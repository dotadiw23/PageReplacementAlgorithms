"""

"""
from algorithms import fifo, lru, opt

class Main():
    print("----------------------------")
    print("--------- Welcome! ---------")
    print("----------------------------")

    do = True
    while(do):

        choose = input("Please choose an option:\n1. FIFO\n2.LRU\n3.OPT\n4.SCA\n5.NRU\n6.Clock\n7.WSClock\n")

        referenceString = input("Please enter the reference String separated by a comma.\n"
                                "For example: 1,2,3,4...,n\n")

        if(choose == '1'):# FIFO algorithm
            algorithm = fifo.Fifo(referenceString)
            algorithm.start()
        elif(choose == '2'): # LRU algorithm
            algorithm = lru.Lru(referenceString)
            algorithm.start()
        elif(choose == '3'): # OPT algorithm
            algorithm = opt.Opt(referenceString)
            algorithm.start()
        elif(choose == '4'): # SCA algorithm
            0
        elif(choose == '5'): # NRU algorithm
            0
        elif(choose == '6'): # Clock algorithm
            0
        elif(choose == '7'): # WSClock algorithm
            0

        # Final decision
        endChoose = input("Press Enter for try another algorithm or N/n to exit... ")
        if(endChoose.casefold() == 'n'):
            print("Thanks for use! ")
            do = False



