"""
LRU algorithm (Least Recently Used).
This algorithm simulates the memory paging of operating system
and outputs the number of page faults.
"""

def searchLeastRecentlyUsed(index, processesQueue, memorySpaces):
    indexes = []
    for i in range(len(memorySpaces)):
        for j in range(index, -1, -1):
            if(memorySpaces[i] == processesQueue[j]):
                #When a process in memory space matches with another
                #process in the processes queue, save the index and search next
                indexes.append(j)
                break
    lruIndex = min(indexes) #Find the index of the least recently used process
    return processesQueue[lruIndex]


referenceString = input("Please enter the reference String separated by a comma.\n"
                        "For example: 1,2,3,4...,n\n")
processesQueue = referenceString.split(",") #input = 1,2,3,3,5,1,2,2,6,2,1,5,7,6,3
                                            #input = 7,0,1,2,0,3,0,4,2,3,0,2,3
memorySpaces = ["","","",""] #For this exercise we have 4 memory spaces
pageFaults = 0

for i in range(len(processesQueue)):
    if not (processesQueue[i] in memorySpaces):
        #Find an an available space in memory
        if (memorySpaces[0] == ""):
            memorySpaces[0] = processesQueue[i]
            pageFaults += 1
        elif (memorySpaces[1] == ""):
            memorySpaces[1] = processesQueue[i]
            pageFaults += 1
        elif (memorySpaces[2] == ""):
            memorySpaces[2] = processesQueue[i]
            pageFaults += 1
        elif (memorySpaces[3] == ""):
            memorySpaces[3] = processesQueue[i]
            pageFaults += 1
        else:
            #When the memory spaces are full, search the least
            #recently used process
            lru = searchLeastRecentlyUsed(i, processesQueue, memorySpaces)
            for j in range(len(memorySpaces)):
                if(memorySpaces[j] == lru):
                    memorySpaces[j] = processesQueue[i]
                    pageFaults += 1
                    break
print(memorySpaces)
print("Page faults: ", pageFaults)