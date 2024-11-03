# musalb: Music Album Organizer

> **Status**: Work in progress

This is a simple command-line tool for managing local album and music files.

## Requirements

- **Python**    
- **FFmpeg**

## Installation (Windows / Linux)
just open a terminal in the project folder and enter:
```
pip install .
```
or if you want the editable mode:

```
pip install -e .
```
if you want to directly run these commands in every shell make sure that python scripts folder is on path

## Usage
|Command|Description|
|-|-|
|`musalb init`|initialize (or re-initialize) musalb album directory entering desired album metadata|
|`musalb reformat`| (after init) apply metadata to every music file |
|`musalb enumerate`|enumerates tracks in alphabetical order (in file metadata)|
|`musalb titles`| for each file copies filename an set it as track title (in file metadata)|