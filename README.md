# ccRegionUtilities 1.12.2
a simple utility scripts for copying, moving, and deleting Minecraft Regions (2dr and 3dr all vertically) within a user's specified bounding box for the __1.12.2__ [Cubic Chunks](https://github.com/OpenCubicChunks/CubicChunks) world.

## Requirements
- Python 3.x (recent versions)


## Usage
- place the script into your world folder
- run the script from console by:
```python scriptname.py```
or:
```python3 scriptname.py```
- input minimum and maximum X and Z coordinates in 2dr Space (Minecraft Region)

## Scripts
- `ccRegionCopy.py` - copies all 2drs and 3drs files from user specified bounding box to `./region2dOutput/` and `./region3dOutput/` in world folder.

- `ccRegionMove.py` - moves all 2drs and 3drs files from user specified bounding box to `./region2dOutput/` and `./region3dOutput/` in world folder.

- `ccRegionMove.py` - deletes all 2drs and 3drs files from user specified bounding box from `./region2d/` and `./region3d/` in world folder.

#### Misc

- `JourneyMapCopyPNG.py` - copies all maptile PNGs from user specified bounding box to `./DIM0_Output/day`.
