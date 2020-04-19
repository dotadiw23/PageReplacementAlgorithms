"""
FIFO algorithm (First Input First Output).
This algorithm simulates the memory paging of operating system
and outputs the number of page faults.
"""

def findFirstInput(memorySpaces, processesQueue):
    inputsOrder = [] #Each index in this array correspond to the index in the memory space

    for i in range (len(memorySpaces)):
        for j in range(len(processesQueue)):
            if(memorySpaces[i] == processesQueue[j]):
                inputsOrder.append(j)
                break

    firstInputIndex = min(inputsOrder) #Filter the min index
    firstInput = processesQueue[int(firstInputIndex)]; #Asing the value of the first input
    processesQueue[int(firstInputIndex)] = "" #Remove the input because now, is an output

    return firstInput

referenceString = input("Please enter the reference String separated by a comma.\n"
                        "For example: 1,2,3,4...,n\n")
processesQueue = referenceString.split(",") #input = 1,2,3,3,5,1,2,2,6,2,1,5,7,6,3
memorySpaces = ["","","",""] #For this exercise we have 4 memory spaces
pageFaults = 0


for i in range(len(processesQueue)):
    if not (processesQueue[i] in memorySpaces):
        #Find an available place in memory to enter the process
        if(memorySpaces[0] == ""):
            memorySpaces[0] = processesQueue[i]
            pageFaults += 1
        elif(memorySpaces[1] == ""):
            memorySpaces[1] = processesQueue[i]
            pageFaults += 1
        elif(memorySpaces[2] == ""):
            memorySpaces[2] = processesQueue[i]
            pageFaults += 1
        elif(memorySpaces[3] == ""):
           memorySpaces[3] = processesQueue[i]
           pageFaults += 1
        else:
            #The memory spaces are full, find first input process
            #to replace it with a new one
            firstInput = findFirstInput(memorySpaces, processesQueue)

            #Finally, allocate the new process in the free memory space
            if (memorySpaces[0] == firstInput):
                memorySpaces[0] = processesQueue[i]
                pageFaults += 1
            elif (memorySpaces[1] == firstInput):
                memorySpaces[1] = processesQueue[i]
                pageFaults += 1
            elif (memorySpaces[2] == firstInput):
                memorySpaces[2] = processesQueue[i]
                pageFaults += 1
            elif (memorySpaces[3] == firstInput):
                memorySpaces[3] = processesQueue[i]
                pageFaults += 1

print(memorySpaces)
print("Pages Faults: ", pageFaults)