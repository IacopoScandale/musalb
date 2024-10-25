from .data.strings import *
import os
import sys


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

  os.chdir(MUSALB_HIDDEN_FOLDER)

  # TODO dump json file  

  raise NotImplementedError


