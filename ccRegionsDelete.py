import os  # to list files in directories
import time  # to count time it takes to finish task

# * this program deletes all 2drs and 3drs files from user specified bounding box in ./region2d/ and ./region3d/
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
# TODO: print the ammount of files that will be deleted from both directories
print(f"The bounding box is {xBoundingBox} x {zBoundingBox} 2d regions large")
if input("Do you want to start the delete process? (y/n)") != "y":
    exit()

# start the timer to count the time it takes to finish the task
startTime = time.process_time()

files2dr = os.listdir("./region2d")
files3dr = os.listdir("./region3d")

for file in files2dr:
        if(file.endswith(".2dr")):
                split = file.split(".")
                x = int(split[0])
                z = int(split[1])
                if(x >= xmin and x <= xmax and z >= zmin and z <= zmax):
                        print(f"Deleting: {x}.{z}.2dr")
                        os.remove(f"./region2d/{x}.{z}.2dr")
for file in files3dr:
        if(file.endswith(".3dr")):
                split = file.split(".")
                x = int(split[0])
                y = int(split[1])
                z = int(split[2])
                if(x >> 1 >= xmin and x >> 1 <= xmax and z >> 1 >= zmin and z >> 1 <= zmax):
                        print(f"Deleting: {x}.{y}.{z}.3dr")
                        os.remove(f"./region3d/{x}.{y}.{z}.3dr")

# print and format the elapsed time for the task
elapsedTime = time.process_time() - startTime
formattedTime = time.strftime("%H:%M:%S", time.gmtime(elapsedTime))
print("Elapsed time: " + formattedTime)
print("Program has finished...")
