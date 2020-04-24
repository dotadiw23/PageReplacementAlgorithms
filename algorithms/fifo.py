"""
FIFO algorithm (First Input First Output).
This algorithm simulates the memory paging of operating system
and outputs the number of page faults.
"""

class Fifo:

    def __init__(self, referenceString):
        self.__memorySpaces = ["","","",""] # For this exercise we have 4 memory spaces
        self.__processesQueue = referenceString.split(",") # input = 1,2,3,3,5,1,2,2,6,2,1,5,7,6,3
        self.__pageFaults = 0

    def findFirstInput(self):
        inputsOrder = []  # Each index in this array correspond to the index in the memory space

        for i in range(len(self.__memorySpaces)):
            for j in range(len(self.__processesQueue)):
                if (self.__memorySpaces[i] == self.__processesQueue[j]):
                    inputsOrder.append(j)
                    break

        firstInputIndex = min(inputsOrder)  # Filter the min index
        firstInput = self.__processesQueue[int(firstInputIndex)];  # Asing the value of the first input
        self.__processesQueue[int(firstInputIndex)] = ""  # Remove the input because now, is an output

        return firstInput


    def start (self):
        for i in range(len(self.__processesQueue)):
            if not (self.__processesQueue[i] in self.__memorySpaces):
                # Find an available place in memory to enter the process
                if (self.__memorySpaces[0] == ""):
                    self.__memorySpaces[0] = self.__processesQueue[i]
                    self.__pageFaults += 1
                elif (self.__memorySpaces[1] == ""):
                    self.__memorySpaces[1] = self.__processesQueue[i]
                    self.__pageFaults += 1
                elif (self.__memorySpaces[2] == ""):
                    self.__memorySpaces[2] = self.__processesQueue[i]
                    self.__pageFaults += 1
                elif (self.__memorySpaces[3] == ""):
                    self.__memorySpaces[3] = self.__processesQueue[i]
                    self.__pageFaults += 1
                else:
                    # The memory spaces are full, find first input process
                    # to replace it with a new one
                    firstInput = self.findFirstInput()

                    # Finally, allocate the new process in the free memory space
                    if (self.__memorySpaces[0] == firstInput):
                        self.__memorySpaces[0] = self.__processesQueue[i]
                        self.__pageFaults += 1
                    elif (self.__memorySpaces[1] == firstInput):
                        self.__memorySpaces[1] = self.__processesQueue[i]
                        self.__pageFaults += 1
                    elif (self.__memorySpaces[2] == firstInput):
                        self.__memorySpaces[2] = self.__processesQueue[i]
                        self.__pageFaults += 1
                    elif (self.__memorySpaces[3] == firstInput):
                        self.__memorySpaces[3] = self.__processesQueue[i]
                        self.__pageFaults += 1

        print(self.__memorySpaces)
        print("Pages Faults: ", self.__pageFaults)
