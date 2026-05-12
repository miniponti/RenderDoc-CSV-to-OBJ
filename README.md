# GameCube RenderDoc OBJ Exporter

A Python script to convert RenderDoc `VS Input` .csv exports from GameCube games into proper `.obj` 3D models with textures.

## Requirements

- Python 3.x (no external libraries needed, uses built-in `csv` module)
- [RenderDoc](https://renderdoc.org/) for capturing and exporting vertex data
- Blender (or any 3D viewer that supports `.obj`) to view the result

## How to Capture the Data in RenderDoc
See `ExtractModels.md` for instructions on how to do this.

## Usage

Run the script from the command line:

```bash
python script.py
