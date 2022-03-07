import os
import pathlib # create directories
import shutil # copy files
import time # process timer

# change working directory to directory of this script, then store it in variable
os.chdir(os.path.dirname(__file__))
workingDirectory = os.getcwd()

terminalSize = os.get_terminal_size()
print("=" * terminalSize.columns)
print("ccRegionManipulate for Cubic Chunks 1.12.2.")
print("Copy, move or delete (.2dr, .3dr) region files within user specified 2d region bounding box range.")
print("Make sure you have backups before doing anything!")
print("CC Worldfixer might be needed to fix light after certain operations.")


### 1. USER INPUT STEPS WITH EXTRA INFORMATION

#TODO maybe add a some notification message if the script haven't found any ./region2d ./region3d input folders?
# user input to choose operation mode
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
            print("This must be a whole number!")
            continue

# user input for X and Z 2d region range (one 2dr region = 512x512 blocks rectangle.)
print("-" * terminalSize.columns)
print("input coordinates in 2dr space range (one 2dr = 512x512 blocks size area):")
while True:
    xMin = integerInput("min x: ")
    xMax = integerInput("max x: ")
    zMin = integerInput("min z: ")
    zMax = integerInput("max z: ")
    # conditions to check if X and Z bounding box input is valid
    if xMin > xMax and zMin > zMax:
        print("'min x' can't be more than 'max x' and")
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

# print X and Z size in 2dr range
xBoundingBox = abs((xMax - xMin) + 1)
zBoundingBox = abs((zMax - zMin) + 1)
print(f"The bounding box is '{xBoundingBox}x{zBoundingBox}' large in 2dr space (Minecraft region coordinates)")

# [optional] user input for Y in 3d region range (one 3dr = 256x256x256 blocks cube)
print("-" * terminalSize.columns)
verticalLimit = False
if input("[optional]: Do you want to set vertical range in 3d region space? (n/y)\n(if you don't, all cubes vertically will be processed) ") == "y":
    print("Input vertical coordinates in 3dr space:")
    print("(one 3dr cube is 256x256x256 blocks)")
    while True:
        yMin = integerInput("min y: ")
        yMax = integerInput("max y: ")
        # condition to check if Y bounding box input is valid
        if yMin > yMax:
            print("'min y' can't be more than 'max y'")
            continue
        if yMin <= yMax:
            verticalLimit = True
            break
    
# prints Y size in 3dr range
if verticalLimit == True:
    yBoundingBox = abs((yMax - yMin) + 1) 
    print(f"Vertical limit range was set as: '{yBoundingBox}' 3dr cubes.\nminimum y 3dr: '{yMin}'.\n maximum y 3dr: '{yMax}'.")
else:
    print("Vertical range limit was not set")


### 2. MAKE LISTS OF FILES NAMES FROM FILTERED INPUT DIRECTORY AND ALL FILES FROM OUTPUT DIRECTORY
###    COUNT NUMBER OF FILES TO BE PROCESSED

#TODO implement file comparision using hashtables for faster processing! 
# list of existing files within user specified range that will be processed
list2drInput = []
list3drInput = []

# list of all existing files in the output directories
list2drOutput = []
list3drOutput = []

# declare variables for the number of processed files
count2dr = 0
count3dr = 0

# get list of all files in the input directories
files2dr = os.listdir("./region2d")
files3dr = os.listdir("./region3d")

# check if output directories exist, then get list of files from the output directories
if os.path.isfile("./region2dOutput"):
    list2drOutput = os.listdir("./region2dOutput")
if os.path.isfile("./region3dOutput"):
    list3drOutput = os.listdir("./region3dOutput")

# count how many 2dr files will be processed before task starts
for file in files2dr:
    if (file.endswith(".2dr")):
        split = file.split(".")
        x = int(split[0])
        z = int(split[1])
        isXMinRange = (x >= xMin)
        isXMaxRange = (x <= xMax)
        isZMinRange = (z >= zMin)
        isZMaxRange = (z <= zMax)
        if (isXMinRange and isXMaxRange and isZMinRange and isZMaxRange):
            count2dr = (count2dr + 1)
            list2drInput.append(file)

# count how many 3dr files will be processed before task starts
for file in files3dr:
    if (file.endswith(".3dr")):
        split = file.split(".")
        x = int(split[0])
        y = int(split[1])
        z = int(split[2])
        isXMinRange = (x >> 1 >= xMin)
        isXMaxRange = (x >> 1 <= xMax)
        isZMinRange = (z >> 1 >= zMin)
        isZMaxRange = (z >> 1 <= zMax)
        # check if vertical range limit was set by user, if true, count within range
        if verticalLimit == True:
            isYMinRange = (y >= yMin)
            isYMaxRange = (y <= yMax)
            if (not isYMinRange or not isYMaxRange):
                continue
        if (isXMinRange and isXMaxRange and isZMinRange and isZMaxRange):
            count3dr = (count3dr + 1)
            list3drInput.append(file)

# create output directories for copy and move modes
# TODO: this could be split to ./region2dCopied or ./region2dMoved depend on the operation mode
if operationMode == "c" or operationMode == "m":
    files2drOutput = pathlib.Path("./region2dOutput")
    files3drOutput = pathlib.Path("./region3dOutput")
    pathlib.Path(files2drOutput).mkdir(parents=True, exist_ok=True)
    pathlib.Path(files3drOutput).mkdir(parents=True, exist_ok=True)

print("-" * terminalSize.columns)
# print the count of total amount of files to be processed
print(f"Total amount of 2dr files to be processed: {count2dr}")
print(f"Total amount of 3dr files to be processed: {count3dr}")


### 3. PROMPT TO CONFIRM WHEN ANY FILES WILL BE OVERWRITTEN

# check for existing files in output directories and prompt user if they want to overwrite files
if os.listdir("./region2dOutput") != [] and os.listdir("./region3dOutput") != []:
    # prompts to print all files that will be overwritten
    if input(f"Do you want to print list of files that will be overwritten? (the list may be very long) (y/n) ") == "y":
        # 2dr file match list
        matches2dr=[]
        for item_a in list2drInput:
            for item_b in list2drOutput:
                if item_a == item_b:
                    matches2dr.append(item_a)
        print("2dr files:")
        print(matches2dr)
        # 3dr file match list
        matches3dr=[]
        for item_a in list3drInput:
            for item_b in list3drOutput:
                if item_a == item_b:
                    matches3dr.append(item_a)
        print("3dr files:")
        print(matches3dr)
        print("Same files were found in input and output directories. ('./region2dOutput/' and './region3dOutput/'.")
        print("Files will be overwritten.")


### 4. TASK PROCESSING

# confirm prompt to start the file processing
print("=" * terminalSize.columns)
print(f"The {operationModeString} operation will be executed in '{workingDirectory}'")
if input(f"Do you want to start the {operationModeString} process? (y/n) ") != "y":
    print("Program terminated.")
    exit()

# start the task timer
startTime = time.time()

# processing of 2dr files
for file in files2dr:
    if (file.endswith(".2dr")):
        split = file.split(".")
        x = int(split[0])
        z = int(split[1])
        isXMinRange = (x >= xMin)
        isXMaxRange = (x <= xMax)
        isZMinRange = (z >= zMin)
        isZMaxRange = (z <= zMax)
        if (isXMinRange and isXMaxRange and isZMinRange and isZMaxRange):
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
        isXMinRange = (x >> 1 >= xMin)
        isXMaxRange = (x >> 1 <= xMax)
        isZMinRange = (z >> 1 >= zMin)
        isZMaxRange = (z >> 1 <= zMax)
        # check if vertical range limit was set by user, if true, process within range
        if verticalLimit == True:
            isYMinRange = (y >= yMin)
            isYMaxRange = (y <= yMax)
            if (not isYMinRange or not isYMaxRange):
                continue
        if (isXMinRange and isXMaxRange and isZMinRange and isZMaxRange):
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


### 5. INFO ABOUT FINISHED TASK

# task duration info at the end
elapsedTime = time.time() - startTime
formattedTime = time.strftime("%H:%M:%S", time.gmtime(elapsedTime))
print(f"2dr files processed: {count2dr}, 3dr files processed: {count3dr}")
print("Elapsed time: " + formattedTime)
print("Program has finished...")

