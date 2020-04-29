"""
SC algorithm (Second Chance).
This algorithm simulates the memory paging of operating system
and outputs the number of page faults.
"""
class Sca:

    def __init__(self, referenceString):
        self.__procesesQueue = referenceString.split(",")  # input = 2,3,2,1,5,2,4,5,3,2,5,2
        self.__memorySpaces = ["", "", ""]  # For this exercise we have 4 memory spaces
        self.__referenceBit = ["", "", ""]  # One bit space for each memory space
        self.__pageFaults = 0

    def findCandidate(self):
        inputsOrder = [] # Contains the indexes of the candidates

        #Find the position of each process saved in memory
        for i in range (len(self.__memorySpaces)):
            for j in range(len(self.__procesesQueue)):
                if(self.__memorySpaces[i] == self.__procesesQueue[j]):
                    inputsOrder.append(j)
                    break

        firstInput = min(inputsOrder); #Find index of the first input

        #Verify if the candidate has or hasn't a reference bit
        do = True
        while (do):
            for i in range (len(self.__memorySpaces)):
                if(self.__procesesQueue[firstInput] == self.__memorySpaces[i]):
                    if(self.__referenceBit[i] == 1):
                        inputsOrder.pop(inputsOrder.index(firstInput))
                        self.__referenceBit[i] = 0
                        firstInput = min(inputsOrder)
                    else:
                        candidate = self.__procesesQueue[firstInput]
                        self.__procesesQueue[firstInput] = ""
                        do = False

        return candidate

    def start(self):
        for i in range(len(self.__procesesQueue)):
            if not(self.__procesesQueue[i] in self.__memorySpaces):
                #If there is an empty space assign it to the process
                #and set the respective reference bit
                if(self.__memorySpaces[0] == ""):
                    self.__memorySpaces[0] = self.__procesesQueue[i]
                    self.__referenceBit [0] = 0
                    self.__pageFaults += 1
                    print("Time [", i, "]; ", self.__memorySpaces, " References Bits: ", self.__referenceBit)
                elif (self.__memorySpaces[1] == ""):
                    self.__memorySpaces[1] = self.__procesesQueue[i]
                    self.__referenceBit[1] = 0
                    self.__pageFaults += 1
                    print("Time [", i, "]; ", self.__memorySpaces, " References Bits: ", self.__referenceBit)
                elif (self.__memorySpaces[2] == ""):
                    self.__memorySpaces[2] = self.__procesesQueue[i]
                    self.__referenceBit[2] = 0
                    self.__pageFaults += 1
                    print("Time [", i, "]; ", self.__memorySpaces, " References Bits: ", self.__referenceBit)
                else:
                    candidate = self.findCandidate()#Find the first input
                    for j in range(len(self.__memorySpaces)):
                        if(self.__memorySpaces[j] == candidate):
                            self.__memorySpaces[j] = self.__procesesQueue[i]
                            self.__referenceBit[j] = 0  # Set it reference bit to 0
                            self.__pageFaults += 1
                            print("Time [", i, "]; ", self.__memorySpaces, " References Bits: ", self.__referenceBit)
                            break
            else:
                for j in range(len(self.__memorySpaces)):
                    if(self.__procesesQueue[i] == self.__memorySpaces[j]):
                        #When the process repeats, set the respective reference bit to 1
                        self.__referenceBit [j] = 1
                        print("Time [", i, "]; ", self.__memorySpaces, " References Bits: ", self.__referenceBit)
                        break

        print("Page faults: ", self.__pageFaults, "\n")