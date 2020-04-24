"""
LRU algorithm (Least Recently Used).
This algorithm simulates the memory paging of operating system
and outputs the number of page faults.
"""

class Lru():

    def __init__(self, referenceString):
        self.__processesQueue = referenceString.split(",") # For this exercise we have 4 memory spaces
        self.__memorySpaces = ["", "", "", ""]  # For this exercise we have 4 memory spaces
        self.__pageFaults = 0


    def searchLeastRecentlyUsed(self, index):
        indexes = []
        for i in range(len(self.__memorySpaces)):
            for j in range(index, -1, -1):
                if (self.__memorySpaces[i] == self.__processesQueue[j]):
                    # When a process in memory space matches with another
                    # process in the processes queue, save the index and search next
                    indexes.append(j)
                    break
        lruIndex = min(indexes)  # Find the index of the least recently used process
        return self.__processesQueue[lruIndex]

    """referenceString = input("Please enter the reference String separated by a comma.\n"
                            "For example: 1,2,3,4...,n\n")
    processesQueue = referenceString.split(",") #input = 1,2,3,3,5,1,2,2,6,2,1,5,7,6,3
                                                #input = 7,0,1,2,0,3,0,4,2,3,0,2,3
    memorySpaces = ["","","",""] #For this exercise we have 4 memory spaces
    pageFaults = 0"""
    def start(self):
        for i in range(len(self.__processesQueue)):
            if not (self.__processesQueue[i] in self.__memorySpaces):
                # Find an an available space in memory
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
                    # When the memory spaces are full, search the least
                    # recently used process
                    lru = self.searchLeastRecentlyUsed(i)
                    for j in range(len(self.__memorySpaces)):
                        if (self.__memorySpaces[j] == lru):
                            self.__memorySpaces[j] = self.__processesQueue[i]
                            self.__pageFaults += 1
                            break
        print(self.__memorySpaces)
        print("Page faults: ", self.__pageFaults, "\n\n")

