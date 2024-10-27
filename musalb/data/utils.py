from .strings import *
import os
import sys


# def create_album_metadata_json() -> None:
#   """
#   Make sure to call this function inside a musalb folder.

#   It is going to create
#   """
#   raise NotImplementedError


def print_enumerate_audio_tracks() -> None:
  """
  prints and enumerates every audio track in the current directory
  """
  counter: int = 0
  for filename in os.listdir():
    if filename.endswith(SUPPORTED_AUDIO_EXT):
      counter += 1
      print(f"{counter:>4}. {filename}")
  print()