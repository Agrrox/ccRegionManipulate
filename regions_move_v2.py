import os  # to list files in directories
import pathlib  # to make directories
import shutil  # to copy files
import time  # to count time it takes to finish task

# * this program moves all 2drs and 3drs files from user specified bounding box to a new folders named ./region2dOutput/ and ./region3dOutput/
# TODO: loop input directory and compare them with output directory, if any files matches, prompt user to confirm to do file overwrite.
# ! MAKE SURE YOU HAVE BACKUPS BEFORE DOING ANYTHING!

# input for min and max 2dr (region) coordinates
# TODO: check if user's input is correct, if not, do exception | i.e if minX is higher than maxX warn user and ask again for input.
# TODO: redo this so it raises exception and handle this properly
print("Input coordinates in 2dr space")
xmin = int(input("min x: "))
xmax = int(input("max x: "))
if (xmin > xmax):
    exit("'min x' can't be more than 'max x'")
zmin = int(input("min z: "))
zmax = int(input("max z: "))
if (xmin > xmax):
    exit("'min z' can't be more than 'max z'")

# get the inclusive bounding box size
xBoundingBox = abs((xmax - xmin) + 1)
zBoundingBox = abs((zmax - zmin) + 1)

# print size of bounding box and prompt user if they want to conitnue
# TODO: print the ammount of files that will be moved to both directories
print(f"The bounding box is {xBoundingBox} x {zBoundingBox} 2d regions large")
if input("Do you want to start the copy process? (y/n)") != "y":
    exit()

# start the timer to count the time it takes to finish the task
startTime = time.process_time()

# lists files in directories
files2dr = os.listdir("./region2d")
files3dr = os.listdir("./region3d")
# assign output paths to variables
files2drOutput = pathlib.Path("./region2dOutput")
files3drOutput = pathlib.Path("./region3dOutput")

# trying some exception handling wether output directory exists or not
if not files2drOutput.exists():
    print("directory /region2dOutput not exists, creating directory and moving files...")
if files2drOutput.exists():
    print("directory /region2dOutput exists, moving files...")

# start process timer to measure time it takes to finish the task
processTime2dr = time.process_time()

# create new directory for 2dr copy output
pathlib.Path(files2drOutput).mkdir(parents=True, exist_ok=True)
# loop each file name from the list
for file in files2dr:
    # checks if file ends with .2dr extension
    if(file.endswith(".2dr")):
        # split file name on dot
        split = file.split(".")
        x = int(split[0])
        z = int(split[1])
        # assign variable to condition check on user's input
        xminRange = (x >= xmin)
        xmaxRange = (x <= xmax)
        zminRange = (z >= zmin)
        zmaxRange = (z <= zmax)
        # checks if all conditions are met
        if (xminRange and xmaxRange and zminRange and zmaxRange):
            # move files from source directory to destination directory
            print(f"Copying: {x}.{z}.2dr")
            shutil.move(f"./region2d/{x}.{z}.2dr",
                        f"./region2dOutput/{x}.{z}.2dr")

# similar operation like above, but with y coordinate added to handle all 3dr files vertically
pathlib.Path(files3drOutput).mkdir(parents=True, exist_ok=True)
for file in files3dr:
    if(file.endswith(".3dr")):
        split = file.split(".")
        x = int(split[0])
        y = int(split[1])
        z = int(split[2])
        xminRange = (x >> 1 >= xmin)
        xmaxRange = (x >> 1 <= xmax)
        zminRange = (z >> 1 >= zmin)
        zmaxRange = (z >> 1 <= zmax)
        if(xminRange and xmaxRange and zminRange and zmaxRange):
            print(f"Copying: {x}.{y}.{z}.3dr")
            shutil.move(f"./region3d/{x}.{y}.{z}.3dr",
                        f"./region3dOutput/{x}.{y}.{z}.3dr")

# print and format the elapsed time for the task
elapsedTime = time.process_time() - startTime
formattedTime = time.strftime("%H:%M:%S", time.gmtime(elapsedTime))
print("Elapsed time: " + formattedTime)
print("Program has finished...")
