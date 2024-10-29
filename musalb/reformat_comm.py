from .data.strings import *
from .data.utils import print_enumerate_audio_tracks
import os
import sys
import json
import subprocess


def apply_metadata(musalb_metadata_json: dict, quiet: bool) -> None:
  """
  apply musalb metadata to every music track in the album
  """
  # assemble ffmpeg command
  ffmpeg_command = 'ffmpeg -hide_banner -i "{in_track}"'
  cover_file: str = musalb_metadata_json.pop("cover")
  if cover_file != "":
    ffmpeg_command += f' -i "{cover_file}" -map 0:0 -map 1 -c:a copy -c:v mjpeg -map_metadata 0'
  else:
    ffmpeg_command += " -c:a copy -map_metadata 0"

  # apply metadata
  for key, value in musalb_metadata_json.items():
    if value != "":
      ffmpeg_command += f' -metadata {key}="{value}"'
  # cover metadata
  if cover_file != "":
    ffmpeg_command += f' -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)"'

  ffmpeg_command += ' "{out_track}"'

  # apply ffmpeg command to every file
  for filename in sorted(os.listdir()):
    if filename.endswith(SUPPORTED_AUDIO_EXT):
      tmp_filename: str = f"tmp_{filename}"
      cur_command = ffmpeg_command.format(
        in_track=filename, 
        out_track=tmp_filename
      )
      
      # terminal becomes a mess: implemented --quiet option
      stderr: int | None = subprocess.DEVNULL if quiet else None
      subprocess.run(cur_command, shell=True, stderr=stderr)

      # if all went good it is time to delete old file and rename new tmp
      os.remove(filename)
      os.rename(tmp_filename, filename)


def print_metadata(musalb_metadata_json: dict) -> None:
  """
  shows all key-value metadata pairs of the musalb album (not shown
  those pairs with value=="")
  """
  print("\nMusalb Refactor: apply following metadata to every track:")
  for key, value in musalb_metadata_json.items():
    if value != "":
      print(f"  - {key:<8} -->   {value}")
  print()


def reformat_comm(album_directory: str, quiet: bool) -> None:
  """
  Apply (using ffmpeg) musalb metadata json (requires that album folder
  is already initialized) to every music track in the album
  """
  os.chdir(album_directory)
  print_enumerate_audio_tracks()

  # requires initialized .musalb folder
  if not os.path.exists(MUSALB_HIDDEN_FOLDER):
    print("\nThis album folder is not initialized")
    print("Use 'musalb init' first")
    sys.exit()
  
  # read metadata from json
  with open(MUSALB_METADATA_JSON, "r") as jsonfile:
    musalb_metadata_json: dict = json.load(jsonfile)
  # print what is going to change
  print_metadata(musalb_metadata_json)

  proceed_choice: str = input(
    "Do you want to reformat this album ? \n"
    "  [Y,n]: "
  )
  if proceed_choice in "sSyY":
    apply_metadata(musalb_metadata_json, quiet)