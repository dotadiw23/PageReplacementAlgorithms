"""
Optimal Page Replacement Algorithm (OPT).
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

def searchCandidate(index, processesQueue, memorySpaces):
    candidates = []  # Save the indexes of the candidates processes
    noMatches = []  # Save the processes that were not found
    match = True

    for i in range(len(memorySpaces)):
        match = True
        for j in range(index, len(processesQueue)):
            if not (memorySpaces[i] == processesQueue[j]):
                if (j == len(processesQueue) - 1 and match == True):
                    # When the process will not be used again
                    # append it in the list of no matches
                    noMatches.append(memorySpaces[i])
            else:
                # When the possible candidate make a coincidence with an element in
                # the processes queue, add to the candidates list
                match = False
                candidates.append(j)
    if (len(noMatches) > 0):
        # Find the candidate using FIFO
        return findFirstInput(noMatches, processesQueue)
    else:
        candidate = max(candidates)  # Find the farthest non used process in the queue
        return processesQueue[candidate]  # Return the process that must to be replaced

referenceString = input("Please enter the reference String separated by a comma.\n"
                        "For example: 1,2,3,4...,n\n")
processesQueue = referenceString.split(",")  # input = D,C,B,A,D,C,E,D,C,B,A,E
memorySpaces = ["", "", "", ""]  # For this exercise we have 3 memory spaces
pageFaults = 0

for i in range(len(processesQueue)):
    if not (processesQueue[i] in memorySpaces):
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
            candidate = searchCandidate(i, processesQueue, memorySpaces)
            for j in range(len(memorySpaces)):
                if (memorySpaces[j] == candidate):
                    memorySpaces[j] = processesQueue[i]
                    pageFaults += 1
                    break;

print(memorySpaces)
print("Pages faults: ", pageFaults)