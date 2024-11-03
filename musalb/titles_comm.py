from .data.utils import print_enumerate_audio_tracks
from .data.strings import SUPPORTED_AUDIO_EXT
import os
import subprocess


def titles_comm() -> None:
  """
  copies filename string and use it as metadata file title
  """
  print_enumerate_audio_tracks()

  choice: str = input(
    "Do you want to use these filenames as metadata titles?\n  [Y,n]: "
  )
  if choice in "sSyY":
    title_comm: str = 'ffmpeg -i "{in_file}" -c copy -map_metadata 0 -metadata title="{title}" "{out_file}"'

    for filename in os.listdir():
      if filename.endswith(SUPPORTED_AUDIO_EXT):
        tmp_filename: str = f"tmp_{filename}"
        title: str = os.path.splitext(filename)[0]
        try:
          subprocess.run(
            title_comm.format(
              in_file=filename, 
              title=title, 
              out_file=tmp_filename
            ),
            shell=True,
            stderr=subprocess.DEVNULL,
          )
        except Exception as e:
          print(e)
          continue

        os.remove(filename)
        os.rename(tmp_filename, filename)

    print("\nDone!")