# jSON-Merger

##### Algorithmic Complexity - O(N) 

##### N - Number of combinations

### There are 2 files present

**File 1 - main.py**

*This is the main driver file.*

It contains two functions:
- find(path,base): Checks if the file exists. 

path = file path 

base = Input file base name

- merge(path,inputBase, outputBase, maxSize):

#### Uses Sliding Window Technique to find the optimal combination

This function finds the combinations for merging.

path = File path

inputBase = Input File base name

outputBase = Output File base name

maxSize = Maximum File size specified by the user

Once the combinations are found, the function called CreateFile() from writer.py

**File 2 - writer.py**

*Responsible for writing file to disk and contains function CreateFile()*

-CreateFile(part,path,out,sizeMapper)

part - The array containing file combinations

path - file path

out - output file base name

sizeMapper - A dictionary which maps filesize to filename.

Sample Execution:
Run main.py
(Example Screenshot is given below)
![alt text](https://github.com/drstrange11/jSON-Merger/blob/master/sample.PNG)
