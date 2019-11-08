import json
from collections import OrderedDict

# Function to write file to disk


def CreateFile(part, path, out, sizeMapper):
    jsonKeys = []  # Stores the unique keys
    jsonItems = []  # Stores the merged json
    for count, size in enumerate(part):
        # Writing merged files to disk
        if len(size) != 1:
            for innerSize in size:
                fileName = sizeMapper[innerSize]
                with open(fileName) as jsonFile:
                    jsonData = json.load(jsonFile)
                    jsonKeys.append(*jsonData.keys())
                    jsonItems.append(*jsonData.items())
            jsonKeys = list(OrderedDict.fromkeys(jsonKeys))
            finalJson = {key: [] for key in jsonKeys}
            for item in jsonItems:
                finalJson[item[0]] += item[1]
            with open(f"{path}/{out}{count+1}.json", "w") as file:
                print(
                    f"\nMerged and written as {out}{count+1}.json. File Size = {len(json.dumps(finalJson))} bytes")
                file.write(json.dumps(finalJson))
        else:
            # Writing files which cannot be merged
            fileName = sizeMapper[size[0]]
            with open(fileName) as jsonFile:
                jsonData = json.load(jsonFile)
            with open(f"{path}/{out}{count+1}.json", "w") as file:
                print(
                    f"\nWritten as {out}{count+1}.json. File Size = {len(json.dumps(jsonData))} bytes")
                file.write(json.dumps(jsonData))
        jsonKeys.clear()
        jsonItems.clear()
