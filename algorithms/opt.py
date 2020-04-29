"""
Optimal Page Replacement Algorithm (OPT).
This algorithm simulates the memory paging of operating system
and outputs the number of page faults.
"""
class Opt:

    def __init__(self, referenceString):
        self.__processesQueue = referenceString.split(",") # input = D,C,B,A,D,C,E,D,C,B,A,E
        self.__memorySpaces = ["", "", ""]  # For this exercise we have 4 memory spaces
        self.__pageFaults = 0


    def findFirstInput(self):
        inputsOrder = [] #Each index in this array correspond to the index in the memory space

        for i in range (len(self.__memorySpaces)):
            for j in range(len(self.__processesQueue)):
                if(self.__memorySpaces[i] == self.__processesQueue[j]):
                    inputsOrder.append(j)
                    break

        firstInputIndex = min(inputsOrder) #Filter the min index
        firstInput = self.__processesQueue[int(firstInputIndex)]; #Asing the value of the first input
        self.__processesQueue[int(firstInputIndex)] = "" #Remove the input because now, is an output

        return firstInput

    def searchCandidate(self, index):
        candidates = []  # Save the indexes of the candidates processes
        noMatches = []  # Save the processes that were not found
        match = True

        for i in range(len(self.__memorySpaces)):
            for j in range(index, len(self.__processesQueue)):
                if not (self.__memorySpaces[i] == self.__processesQueue[j]):
                    if (j == len(self.__processesQueue) - 1 and match == True):
                        # When the process will not be used again
                        # append it in the list of no matches
                        noMatches.append(self.__memorySpaces[i])
                else:
                    # When the possible candidate make a coincidence with an element in
                    # the processes queue, add to the candidates list
                    match = False
                    candidates.append(j)
        if (len(noMatches) > 0):
            # Find the candidate using FIFO
            return self.findFirstInput()
        else:
            candidate = max(candidates)  # Find the farthest non used process in the queue
            return self.__processesQueue[candidate]  # Return the process that must to be replaced

    def start(self):
        for i in range(len(self.__processesQueue)):
            if not (self.__processesQueue[i] in self.__memorySpaces):
                if (self.__memorySpaces[0] == ""):
                    self.__memorySpaces[0] = self.__processesQueue[i]
                    self.__pageFaults += 1
                    print("Time [", i, "]:", self.__memorySpaces)
                elif (self.__memorySpaces[1] == ""):
                    self.__memorySpaces[1] = self.__processesQueue[i]
                    self.__pageFaults += 1
                    print("Time [", i, "]:", self.__memorySpaces)
                elif (self.__memorySpaces[2] == ""):
                    self.__memorySpaces[2] = self.__processesQueue[i]
                    self.__pageFaults += 1
                    print("Time [", i, "]:", self.__memorySpaces)
                else:
                    candidate = self.searchCandidate(i)
                    for j in range(len(self.__memorySpaces)):
                        if (self.__memorySpaces[j] == candidate):
                            self.__memorySpaces[j] = self.__processesQueue[i]
                            self.__pageFaults += 1
                            print("Time [", i, "]:", self.__memorySpaces)
                            break;

        print(self.__memorySpaces)
        print("Pages faults: ", self.__pageFaults, "\n")