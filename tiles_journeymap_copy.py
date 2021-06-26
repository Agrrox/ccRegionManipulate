import os
import pathlib  # to make directories
import shutil  # to copy files

# min max bouding box input from a user
print("Input coordinates in MC regions space")
xmin = int(input("min x: "))
xmax = int(input("max x: "))
zmin = int(input("min z: "))
zmax = int(input("max z: "))

# lists files in directory
filesPNG = os.listdir("./DIM0/day/")
# set path for output
filesPNGoutput = pathlib.Path("./DIM0_Output/day")

#trying some exception handling here
if not filesPNGoutput.exists():
    print("directory /DIM0_Output not exists, creating directory and moving files...")
if filesPNGoutput.exists():
    print("directory /DIM0_Output exists, moving files...")

# create new directory for PNG copy output    
pathlib.Path(filesPNGoutput).mkdir(parents=True, exist_ok=True)

# loop each PNG contained within the bounding box
for file in filesPNG:
    if(file.endswith(".png")):
        splitDot = file.split(".")
        splitComma = splitDot[0].split(",")
        x = int(splitComma[0])
        z = int(splitComma[1])
        if(x >= xmin and x <= xmax and z >= zmin and z <= zmax):
            print(f"Copying: {x},{z}.png")
            shutil.copy(f"./DIM0/day/{x},{z}.png",
                        f"./DIM0_Output/day/{x},{z}.png")

print("Done...")