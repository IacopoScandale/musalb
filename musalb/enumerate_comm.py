from .data.utils import print_enumerate_audio_tracks
from .data.strings import *
import os
import subprocess


def enumerate_comm() -> None:
  print_enumerate_audio_tracks()
  enum_choice: str = input(
    "Do you want to enumerate them in the shown order?\n  [Y,n]: "
  )
  if enum_choice in "sSyY":
    print("Enumerating: ...")
    counter: int = 0
    command = 'ffmpeg -hide_banner -i "{in_file}" -c copy -map_metadata 0 -metadata track={n}  "{out_file}"'
    for filename in sorted(os.listdir()):
      if filename.endswith(SUPPORTED_AUDIO_EXT):
        counter += 1
        tmp_filename: str = f"tmp_{filename}"

        subprocess.run(
          command.format(in_file=filename, n=counter, out_file=tmp_filename),
          shell=True, 
          stderr=subprocess.DEVNULL,
        )
        os.remove(filename)
        os.rename(tmp_filename, filename)
    print("Done!")