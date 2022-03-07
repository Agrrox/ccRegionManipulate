# ccRegionManipulate for Cubic Chunks 1.12.2
a user-friendly python scripts which allow you to copy, move or delete regions (2dr + 3dr files) in 1.12.2 cubic chunks worlds within a user's specified range of bounding boxe. 
This script is only for the __1.12.2__ [Cubic Chunks](https://github.com/OpenCubicChunks/CubicChunks) worlds.

## Requirements
- Python 3.x (recent versions)


## Starting the program
- place the script into your world folder
- run the script from console by:

```python ccRegionManipulate.py```

if you on macOS or Linux:

```python3 ccRegionManipulate.py``` - (built-in python2 is not sufficient, install recent version of [Python 3](https://www.python.org/))

### Usage
- choose one of the operation mods, either `copy` `move` or `delete`
- input `minimum and maximum X and Z` coordinates in 2dr space area (in Minecraft Region coordinates) which will be processed by the program
- [optional] choose vertical range limit, skip this with `no` if you want everything to be processed vertically from top to bottom.

##  Example of usage of the program
<details> <summary>SPOILER</summary> 

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
