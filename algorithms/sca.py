"""
SC algorithm (Second Chance).
This algorithm simulates the memory paging of operating system
and outputs the number of page faults.
"""

def findCandidate(procesessQueue, memorySpaces, referenceBit):
   0


referenceString = input("Please enter the reference String separated by a comma.\n"
                        "For example: 1,2,3,4...,n\n")
processesQueue = referenceString.split(",") #input = 2,3,2,1,5,2,4,5,3,2,5,2
memorySpaces = ["","",""] #For this exercise we have 4 memory spaces
referenceBit = ["","",""] #One bit space for each memory space
pageFaults = 0

for i in range(len(processesQueue)):
    if not(processesQueue[i] in memorySpaces):
        #If there is an empty space assign it to the process
        #and set the respective reference bit
        if(memorySpaces[0] == ""):
            memorySpaces[0] = processesQueue[i]
            referenceBit [0] = 0
            pageFaults += 1
        elif (memorySpaces[1] == ""):
            memorySpaces[1] = processesQueue[i]
            referenceBit[1] = 0
            pageFaults += 1
        elif (memorySpaces[2] == ""):
            memorySpaces[2] = processesQueue[i]
            referenceBit[2] = 0
            pageFaults += 1
        else:
            candidate = findCandidate(processesQueue, memorySpaces, referenceBit)#Find the first input
            for j in range(len(memorySpaces)):
                if(memorySpaces[j] == candidate):
                    memorySpaces[j] = processesQueue[i]
                    referenceBit[j] = 0  # Set it reference bit to 0
                    pageFaults += 1
                    break
    else:
        for j in range(len(memorySpaces)):
            if(processesQueue[i] == memorySpaces[j]):
                #When the process repeats, set the respective reference bit to 1
                referenceBit [j] = 1
                break

print(memorySpaces)
print("Page faults: ", pageFaults)