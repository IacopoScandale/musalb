from .data.strings import *
from .data.utils import print_enumerate_audio_tracks
import os
import sys
import json


def find_cover() -> str:
  """
  Finds in the current folder a file ending in:
  - ".jpg"
  - ".jpeg"
  - ".png"

  and returns its filename. If not found returns empty string "". 
  
  TLDR: Returns the first image name found in a folder. So if we are
  used to put in an album folder the cover file, then it will be used
  as cover.
  """
  for filename in os.listdir():
    if filename.endswith(IMAGE_COVER_EXT):
      return filename
    
  return ""


def enter_album_metadata() -> tuple[str, str, str, str, str]:
  """
  Prints every track in the album and ask you to enter album metadata:

  - `album` 
  - `artist` 
  - `date`
  - `enumerate_choice` if Yes (default ) then every music track is going
    to have that enumeration shown previously 
  - `cover` cover image filename inside folder or "" if not found or if
    user does not want to apply it to every music track
  """
  # enumerate tracks
  print_enumerate_audio_tracks()

  # enter metadata
  try:
    album: str = input("\n 1/5: Insert album name or leave it blank:\n      ")
    artist: str = input("\n 2/5: Insert artist or leave it blank:\n      ")
    date: str = input("\n 3/5: Insert album date or leave it blank:\n      ")
    enumerate_choice: str = input(
      (
        "\n 4/5: Do you want to enumerate them in the shown order?"
        "\n      [Y,n]: "
      )
    )
    cover_choice: str = input(
      (
        "\n 5/5: Use the only image in the folder as album cover for each file?"
        "\n      (if not present drag it in the folder now)"
        "\n      [Y,n]: "
      )
    )
  except KeyboardInterrupt:
    sys.exit()

  cover: str = find_cover() if cover_choice in "sSnN" else ""

  return (album, artist, date, enumerate_choice, cover)


def init_comm(album_directory: str) -> None:
  """
  initialize or reinitialize a musalb music folder:

  a musalb music folder is a simple music folder that contains the
  hidden folder `.musalb`

  this function is going to create that folder and will ask for album
  metadata
  """
  os.chdir(album_directory)
  # create .musalb folder if it not exists
  if not os.path.exists(MUSALB_HIDDEN_FOLDER):
    os.mkdir(MUSALB_HIDDEN_FOLDER)
  else:
    choice: str = input(
      "This album is already initialized. Do you want to "
      "re-initialize it?\n  [Y,n]: "
    )
    if choice in "yYsS":
      pass
    else:
      sys.exit()

  # create musalb metadata json file  
  # TODO use enumerate_choice or delete it
  album, artist, date, enumerate_choice, cover = enter_album_metadata()
  musalb_metadata_json = dict()
  musalb_metadata_json["album"] = album
  musalb_metadata_json["artist"] = artist
  musalb_metadata_json["date"] = date
  musalb_metadata_json["cover"] = cover

  with open(MUSALB_METADATA_JSON, "w") as jsonfile:
    json.dump(musalb_metadata_json, jsonfile, indent=2)
