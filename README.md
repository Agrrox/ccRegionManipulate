# ccRegionManipulate
a simple python script which allows you to copy, move or delete region files (2dr + 3dr) in a 1.12.2 Cubic Chunks worlds within specified 3dr bounding box ranges.

*This script is only for the 1.12.2 [Cubic Chunks](https://github.com/OpenCubicChunks/CubicChunks) worlds.*

## Prequisites
- [Python 3](https://www.python.org/)


## Installation
- place the script inside your world folder that you want to process
- run the script from command-line interface:

```python ccRegionManipulate.py```

if you on macOS or Linux:

```python3 ccRegionManipulate.py``` - (mac comes with pre-installed python 2 that is not sufficient, get [Python 3](https://www.python.org/))

## Usage

**1. choose operation mode:**
- `c` - to copy regions into `./region2dOutput` and `./region3dOutput`
- `m` - to move regions into `./region2dOutput` and `./region3dOutput`
- `d` - to delete regions

**2. input coordinates in 2dr space range (MC Region coordinates, 512x512 blocks):**
- `minimum X`
- `maximum X` 
- `minimum Z`
- `maximum Z`

**3. [optional] set vertical range in 3dr space range (256x256x256 blocks):**
- `n` if you want process everything from top to bottom.
- `y` if you want to set vertical limit:
   - `minimum Y`
   - `maximum Y`

**4. confirm to start processing.**

##  Example of use

<details> <summary></summary> 

  ```
user$ python3 /users/username/minecraft/New World/ccRegionManipulate_mc1.12.2.py 
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
[optional]: Do you want to set vertical range in 3dr (256x256x256 cubes) space? (n/y)
(if you don't, all cubes vertically will be processed) n
Vertical range limit was not set
--------------------------------------------------------------------------------
Total number of 2dr files to be processed: 241
Total number of 3dr files to be processed: 1670
--------------------------------------------------------------------------------
The copy operation will be executed in '/users/username/minecraft/New World/'
Do you want to start the copy process? (y/n) n

```
</details>
