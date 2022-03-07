# ccRegionManipulate
a user-friendly python script which allows you to copy, move or delete region files (2dr + 3dr) in a 1.12.2 Cubic Chunks worlds within specified 2dr bounding box range.     __This script is only for the 1.12.2 [Cubic Chunks](https://github.com/OpenCubicChunks/CubicChunks) worlds.__

## Prequisites:
- recent version of Python 3


## Installation:
- place the script into folder of your world (script in same folder that contain region2d and region3d folders)
- run the script from command-line interface by:

```python ccRegionManipulate.py```

if you on macOS or Linux:

```python3 ccRegionManipulate.py``` - (built-in python 2 is not sufficient, install recent version of [Python 3](https://www.python.org/))

## Use of the program:
1. choose one of the operation mods by typing:
- `c` = copy regions (to `./region2dOutput` and `./region3dOutput`)
- `m` = move regions (to `./region2dOutput` and `./region3dOutput`)
- `d` = delete regions

2. input coordinates in 2dr space area (in Minecraft Region coordinates)
- `minimum X`
- `maximum X` 
- `minimum Z`
- `maximum Z` 
3. [optional] choose vertical range limit, skip this with `no` if you want everything to be processed vertically from top to bottom.

##  Example of use:
<details> <summary></summary> 

  ```
user$ python3 /users/username/minecraft/New World/ccRegionManipulate_mc1.12.2.py 
================================================================================
ccRegionManipulate for Cubic Chunks 1.12.2.
Copy, move or delete Minecraft regions in specific range.
to use this program, please put this script into your world folder
Make sure you have backups before doing anything!
You might need to fix the light using cc worldfixer after some operations.
================================================================================
Possible operation modes:
'c' = copy regions | 'm' = move regions | 'd' = delete regions
Choose an operation mode: c
'copy' mode was selected.
--------------------------------------------------------------------------------
Input coordinates in 2dr space (Minecraft region coordinates):
min x: 20
max x: 200
min z: 10
max z: 300
The bounding box is '181x291' large in 2dr space
--------------------------------------------------------------------------------
[optional]: Do you want to set vertical range in 3dr (cube) space? (n/y)
(if you don't, all cubes vertically will be processed) n
Vertical range limit was not set
--------------------------------------------------------------------------------
Total number of 2dr files to be processed: 241
Total number of 3dr files to be processed: 1670
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
The copy operation will be executed in '/users/username/minecraft/New World/'
Do you want to start the copy process? (y/n) n

```
</details>

##  TODO
- add option to choose between 2dr and 3dr range.
