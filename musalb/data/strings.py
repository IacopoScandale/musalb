import os


MUSALB_HIDDEN_FOLDER: str = ".musalb"
MUSALB_METADATA_JSON: str = os.path.join(
  MUSALB_HIDDEN_FOLDER, 
  "musalb_metadata.json"
)
"""
Relative path of musalb metadata json from album folder

In the key-value pairs, if a value is "" then just ignore that field

TODO handle same album different years and comments
-> maybe use base data like album artist etc than for specific piece
   use specific metadata 

- `'album' -> str` is the album name

- `'artist' -> str` is the artist name

- `'cover' -> str` name of the cover file e.g. 'cover.jpg'

- `'date' -> int` year
"""

SUPPORTED_AUDIO_EXT: tuple[str] = (".mp3", ".aac", ".flac")
IMAGE_COVER_EXT: tuple[str] = (".jpg",".jpeg",".png")