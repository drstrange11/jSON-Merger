import json
import glob
from writer import CreateFile

# Function to find if the file is present in the directory specified


def Find(path, base):
    pathLength = len(path)
    try:
        files = glob.glob(f"{path}/{base}*.json")  # Searching for the file
    except FileNotFoundError:
        return None  # If file is not found, return a prompt to the user
    files = [file[pathLength + 1:]
             for file in files]  # If found, returns the filenames
    return files

# Function to find the files which can be merged


def Merge(path, inputBase, outputBase, maxSize):
    files = Find(path, inputBase)  # To check if the file exists
    if not files:
        print("File Not found")
        return
    print(f"{len(files)} files found.")
    for file in files:  # Prints the filenames
        print(file)
    jsonSize = []  # Stores the file sizes of the json
    partitions = []  # Stores the sizes of the combinations involved in the merge
    sizeMap = {}  # Maps the filesize to the file name
    for fileSuffix in range(1, len(files) + 1):
        fileName = f"{inputBase}{fileSuffix}.json"
        # Loading the json file
        with open(fileName) as jsonFile:
            jsonData = json.load(jsonFile)
            fileSize = len(json.dumps(jsonData))
            jsonSize.append(fileSize)
            sizeMap[fileSize] = fileName
    # If the Maxfilesize specified is greater than current json file, returns
    # error message
    if max(jsonSize) > maxSize:
        print("Wrong Size. Merge not possible.")
    else:
        i = 0
        # Using Sliding window technique to find combinations of the files
        while i < len(jsonSize) - 1:
            currSum = jsonSize[i]
            for j in range(i + 1, len(jsonSize)):
                currSum = currSum + jsonSize[j]
                if currSum > maxSize:
                    partitions.append(jsonSize[i:j])
                    i = j
                    break
            if i == j - 1:
                j -= 1
                break
            if j == len(jsonSize) - 1:
                partitions.append(jsonSize[i:j + 1])
                break
        if j != len(jsonSize) - 1:
            partitions.append(jsonSize[j:])

        # Prints the merge found in an appropriate way
        print(f"\nMaximum file Size specified = {maxSize} bytes\n")
        print(f"Total number of Output files = {len(partitions)}")
        comb = ''
        for count, size in enumerate(partitions):
            if len(size) != 1:
                mergeSize = 0
                for innerSize in size:
                    comb = comb + f"{sizeMap[innerSize]}, "
                    mergeSize += innerSize
                print(
                    f"\n{comb[:-1]} will be merged and written to disk as {outputBase}{count + 1}.json.")
            else:
                print(
                    f"\n{sizeMap[size[0]]} will be as it is and written to disk as {outputBase}{count + 1}.json. Size = {size[0]} bytes")
        # Merges are written back to disk
        CreateFile(partitions, path, outputBase, sizeMap)


# Driver Function
if __name__ == '__main__':
    print("Welcome to JSON Merger")
    path = input("Enter the path: ")
    inputBase = input("Enter the input file base name: ")
    outputBase = input("Enter the output file base name: ")
    maxSize = int(input("Enter the max file size in bytes: "))
    Merge(path, inputBase, outputBase, maxSize)
