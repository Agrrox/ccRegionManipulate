import os
import pathlib # create directories
import shutil # copy files
import time # process timer

# change working directory to directory of this file
os.chdir(os.path.dirname(__file__))
workingDirectory = os.getcwd()

terminalSize = os.get_terminal_size()
print("=" * terminalSize.columns)
print("ccRegionManipulate for Cubic Chunks 1.12.2.")
print("Copy, move or delete Minecraft regions in specific range.")
print("to use this program, please put this script into your world folder")
print("Make sure you have backups before doing anything!")
print("You might need to fix the light using cc worldfixer after some operations.")

# user selects from operation modes
print("=" * terminalSize.columns)
print(f"Possible operation modes:")
print("'c' = copy regions | 'm' = move regions | 'd' = delete regions")
while True:
    operationMode = input("Choose an operation mode: ")
    if operationMode == "c":
        operationModeString = "copy"
        print (f"'{operationModeString}' mode was selected.")
        break
    if operationMode == "m":
        operationModeString = "move"
        print (f"'{operationModeString}' mode was selected.")
        break
    if operationMode == "d":
        operationModeString = "delete"
        print (f"'{operationModeString}' mode was selected.")
        break
    else:
        print(f"Please select a valid operation mode!")

# function to check for non-integer input
def integerInput(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Whole number, please")
            continue

# user input for X and Z 2dr coordinates
print("-" * terminalSize.columns)
print("Input coordinates in 2dr space (Minecraft region coordinates):")
while True:
    xMin = integerInput("min x: ")
    xMax = integerInput("max x: ")
    zMin = integerInput("min z: ")
    zMax = integerInput("max z: ")
    if xMin > xMax and zMin > zMax:
        print("'min x' can't be more than 'max x'")
        print("'min z' can't be more than 'max z'")
        continue
    if xMin > xMax:
        print("'min x' can't be more than 'max x'")
        continue
    if zMin > zMax:
        print("'min z' can't be more than 'max z'")
        continue
    if xMin <= xMax and zMin <= zMax:
        break

# prints size of X and Z 2dr range
xBoundingBox = abs((xMax - xMin) + 1)
zBoundingBox = abs((zMax - zMin) + 1)
print(f"The bounding box is '{xBoundingBox}x{zBoundingBox}' large in 2dr space")

# optional user input for Y 3dr coordinates
print("-" * terminalSize.columns)
verticalLimit = False
if input("[optional]: Do you want to set vertical range in 3dr (cube) space? (n/y)\n(if you don't, all cubes vertically will be processed) ") == "y":
    print("Input vertical coordinates in 3dr space:")
    print("(1 cube unit in 3dr space is 256 blocks)")
    while True:
        yMin = integerInput("min y: ")
        yMax = integerInput("max y: ")            
        if yMin > yMax:
            print("'min y' can't be more than 'max y'")
            continue
        if yMin <= yMax:
            verticalLimit = True
            break
    
# prints size of Y 3dr range
if verticalLimit == True:
    yBoundingBox = abs((yMax - yMin) + 1) 
    print(f"Vertical limit range was set as: '{yBoundingBox}' 3dr cubes.\nminimum y 3dr: '{yMin}'.\n maximum y 3dr: '{yMax}'.")
else:
    print("Vertical range limit was not set")

# define variables for counting processed files
count2dr = 0
count3dr = 0

# define lists for user input range that will be looped 
list2drInput = []
list3drInput = []
# get list of files in input directories # ! apply .2dr and 3.dr filter?
files2dr = os.listdir("./region2d")
files3dr = os.listdir("./region3d")

# define Ouput lists
list2drOutput = []
list3drOutput = []
# get list of files in output directories # ! apply .2dr and 3.dr filter?
if os.path.isfile("./region2dOutput"):
    list2drOutput = os.listdir("./region2dOutput")
if os.path.isfile("./region3dOutput"):
    list3drOutput = os.listdir("./region3dOutput")


# loop 2dr to count all files for info report and file comparison
for file in files2dr:
    if (file.endswith(".2dr")):
        split = file.split(".")
        x = int(split[0])
        z = int(split[1])
        xMinRange = (x >= xMin)
        xMaxRange = (x <= xMax)
        zMinRange = (z >= zMin)
        zMaxRange = (z <= zMax)
        if (xMinRange and xMaxRange and zMinRange and zMaxRange):
            count2dr = (count2dr + 1)
            list2drInput.append(file)

# loop 3dr to count all files for info report and file comparison
for file in files3dr:
    if (file.endswith(".3dr")):
        split = file.split(".")
        x = int(split[0])
        y = int(split[1])
        z = int(split[2])
        xMinRange = (x >> 1 >= xMin)
        xMaxRange = (x >> 1 <= xMax)
        zMinRange = (z >> 1 >= zMin)
        zMaxRange = (z >> 1 <= zMax)
        # treatment if user set a vertical range
        if verticalLimit == True:
            yMinRange = (y >= yMin)
            yMaxRange = (y <= yMax)
            if not(yMinRange or yMaxRange):
                continue
        if (xMinRange and xMaxRange and zMinRange and zMaxRange):
            count3dr = (count3dr + 1)
            list3drInput.append(file)

# creates directories for output when copy or move mode was selected
if operationMode == "c" or operationMode == "m":
    files2drOutput = pathlib.Path("./region2dOutput")
    files3drOutput = pathlib.Path("./region3dOutput")
    pathlib.Path(files2drOutput).mkdir(parents=True, exist_ok=True)
    pathlib.Path(files3drOutput).mkdir(parents=True, exist_ok=True)

print("-" * terminalSize.columns)
# print looped files from the lists that will be processed
print(f"Total number of 2dr files to be processed: {count2dr}")
print(f"Total number of 3dr files to be processed: {count3dr}")      

# check for existing files in output directories and prompt user
print("-" * terminalSize.columns)
if os.listdir("./region2dOutput") and os.listdir("./region3dOutput") != []:
    print("Same files were found in input and output directories. ('./region2dOutput/' and './region3dOutput/'.")
    print("Files will be overwritten.")
    # prompts to print all files that will be overwritten # ! add condition when there are actuall files to be overwritten
    if input(f"Do you want to print list of files that will be overwritten? (the list may be very long) (y/n) ") == "y":
        # 2dr list 
        matches2dr=[]
        for item_a in list2drInput:
            for item_b in list2drOutput:
                if item_a == item_b:
                    matches2dr.append(item_a)
        print("2dr files:")
        print(matches2dr)
        # 3dr list
        matches3dr=[]
        for item_a in list3drInput:
            for item_b in list3drOutput:
                if item_a == item_b:
                    matches3dr.append(item_a)
        print("3dr files:")
        print(matches3dr)

# prompt to start the file processing
print("-" * terminalSize.columns)
print(f"The {operationModeString} operation will be executed in '{workingDirectory}'")
if input(f"Do you want to start the {operationModeString} process? (y/n) ") != "y":
    print("Program terminated.")
    exit()

# process timer
startTime = time.process_time()    

# processing of 2dr files
for file in files2dr:
    if (file.endswith(".2dr")):
        split = file.split(".")
        x = int(split[0])
        z = int(split[1])
        xMinRange = (x >= xMin)
        xMaxRange = (x <= xMax)
        zMinRange = (z >= zMin)
        zMaxRange = (z <= zMax)
        if (xMinRange and xMaxRange and zMinRange and zMaxRange):
            if operationMode == "c":
                print(f"Copying: {x}.{z}.2dr")
                shutil.copy(f"./region2d/{x}.{z}.2dr",
                        f"./region2dOutput/{x}.{z}.2dr")
            if operationMode == "m":
                print(f"Moving: {x}.{z}.2dr")
                shutil.move(f"./region2d/{x}.{z}.2dr",
                        f"./region2dOutput/{x}.{z}.2dr")
            if operationMode == "d":
                print(f"Deleting: {x}.{z}.2dr")
                os.remove(f"./region2d/{x}.{z}.2dr")

# processing of 3dr files
for file in files3dr:
    if (file.endswith(".3dr")):
        split = file.split(".")
        x = int(split[0])
        y = int(split[1])
        z = int(split[2])
        xMinRange = (x >> 1 >= xMin)
        xMaxRange = (x >> 1 <= xMax)
        zMinRange = (z >> 1 >= zMin)
        zMaxRange = (z >> 1 <= zMax)
        # treatment if user set a vertical range
        if verticalLimit == True:
            yMinRange = (y >= yMin)
            yMaxRange = (y <= yMax)
            if not(yMinRange or yMaxRange):
                continue
        if (xMinRange and xMaxRange and zMinRange and zMaxRange):
            if operationMode == "c":
                print(f"Copying: {x}.{y}.{z}.3dr")
                shutil.copy(f"./region3d/{x}.{y}.{z}.3dr",
                            f"./region3dOutput/{x}.{y}.{z}.3dr")
            if operationMode == "m":
                print(f"Moving: {x}.{y}.{z}.3dr")
                shutil.move(f"./region3d/{x}.{y}.{z}.3dr",
                            f"./region3dOutput/{x}.{y}.{z}.3dr")
            if operationMode == "d":
                print(f"Deleting: {x}.{y}.{z}.3dr")
                os.remove(f"./region3d/{x}.{y}.{z}.3dr")

# task information at the end
elapsedTime = time.process_time() - startTime
formattedTime = time.strftime("%H:%M:%S", time.gmtime(elapsedTime))
print(f"2dr files processed: {count2dr}, 3dr files processed: {count3dr}")
print("Elapsed time: " + formattedTime)
print("Program has finished...")
