import random, collections, math
import matplotlib.pyplot as plt
import numpy as np
# This is a program that will generate the statistics behind randomly selecting a card from a deck of 52
# It is designed to help articulate the chances of specific occurences within the game

plt.ioff()
# Define list of each card to help with randomising

# Each card must have a suite and a card value as follows
# A = Spades
# B = Diamonds
# C = Hearts
# D = Clubs

# 1 = Aces
# 2 = 2
# ...
# 10 = 10
# 11 = Jacks
# 12 = Queens
# 13 = Kings

numOfTries = 2000000
def mainMethod():
    cardList = []

    # chr(65) = A -> chr(69) = D
    for x in range(numOfTries):
        currentCardValue = chr(random.randint(65,68)) + str(random.randint(1,13))
        cardList.append(currentCardValue)

    cardList = collections.Counter(cardList)

    plt.title("Poker Hands Test")
    plt.xlabel("Index")

    sortedList = []
    for x in sorted(cardList.iterkeys()):
        sortedList.append(np.divide(cardList[x],float(numOfTries))*100)
    #counter = 1
    #for x in cardList:
    #    print cardList[x]
    x = range(52)
    y = sortedList

    y += ['0'] * (len(x) - len(y))

    dataLine = plt.plot(x,y, label="Raw Data", marker="o")

    print "Average:", np.mean(y)


        #print cardList[x]
    #    counter = counter + 1
    plt.show()




mainMethod()
