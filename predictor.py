import random, collections, math
import matplotlib.pyplot as plt
import numpy as np

# This is a program that will generate the statistics behind randomly selecting a card from a deck of 52
# It is designed to help articulate the chances of specific occurences within the game

# Each card must have a suite and a card value as follows
# A = Spades
# B = Diamonds
# C = Hearts
# D = Clubs

# 10 = Aces
# 12 = 2
# ...
# 20 = 10
# 21 = Jacks
# 22 = Queens
# 23 = Kings

'''
Cards dealt per round = 2 per player, per game + 3 for house per game
 = (2*numOfPlayers)* numOfGames + 3*numOfGames
 = ((numOfGames)*(2*numOfPlayers + 3))
'''


numOfPlayers = 8
numOfDecks = 1
numOfGamesToPlay = 100

class person(object):
    def __init__(self, name=None, card1=None, card2=None):
        self.name = name
        self.card1 = card1
        self.card2 = card2

peopleList = []
peopleNameList = "Nick", "Lilly", "Crystal", "Harry", "J", "Lachlan", "Barry", "Luke", "Noal"
playedCardList = []
shuffledCardsCounter = 0

def findCard():
    global playedCardList
    global shuffledCardsCounter
    # Pick a random card
    currentCard = chr(random.randint(65,68)) + str(random.randint(10,23))

    # Loop until a valid card is chosen
    while(not(playedCardList.count(currentCard) < numOfDecks)):
        currentCard = chr(random.randint(65,68)) + str(random.randint(10,23))
        if(len(playedCardList) >= 52):
            playedCardList = []
            shuffledCardsCounter += 1
        else:
            if(len(playedCardList)>52):
                playedCardList = []
                shuffledCardsCounter += 1
                #print len(playedCardList), playedCardList

    # Once exited loop correct card will be chosen
    # Append to array, return card
    playedCardList.append(currentCard)
    return currentCard

def findBestCombination(card1, card2, card3, card4, card5, card6, card7):
    # Poker Hands:
    # Pair
    # Two Pair
    # Three of a kind
    # Straight
    # Full House (pair + 3 of a kind)
    # Straight flush
    # Royal flush
    #  ***** Now for the time being for simplicity we will only focus on pair, two pair, three of a kind and full House *****

    # Start slicing start of strings in order to remove family of card
    card1 = card1[1:]
    card2 = card2[1:]
    card3 = card3[1:]
    card4 = card4[1:]
    card5 = card5[1:]
    card6 = card6[1:]
    card7 = card7[1:]

    activeList = [card1, card2, card3, card4, card5, card6, card7]
    activeList = collections.Counter(activeList).most_common(3)
    activeList2 = activeList

    previousValue = 0
    result = "initError"
    for value in activeList:
        # Select appropriate value from array at index 1
        value = value[1]
        if(result == "initError"):
            if(value == 4):
                previousValue = 4
                result = "Four of a kind"
            elif(value == 3):
                previousValue = 3
            elif(value == 2):
                if(previousValue == 3):
                    previousValue = 2
                    result = "Full House"
                elif(previousValue == 2):
                    previousValue = 2
                    result = "Two Pair"
                elif(previousValue == 1):
                    previousValue = 2
                    result = "Pair"
                elif(previousValue == 0):
                    previousValue = 2
                else:
                    result = "Error"
            elif(value == 1):
                if(previousValue == 3):
                    previousValue = 1
                    result = "Three of a kind"
                elif(previousValue == 2):
                    previousValue = 1
                    result = "Pair"
                else:
                    result = "No Pair"
            else:
                print "******"
                print previousValue
                print value
                print activeList
                print card1
                print card2
                print card3
                print card4
                print card5
                print "*******"
                result = "Error"

    # Once iterated through results, return final result
    return result


def mainMethod():
    currentGame = 0
    noPair = 0
    onePair = 0
    twoPair = 0
    threeOfKind = 0
    fullHouse = 0
    fourOfKind = 0
    while(currentGame < numOfGamesToPlay):
        # Begin by defining game players
        for x in range(numOfPlayers):
            personEntity = person()
            personEntity.name = peopleNameList[random.randint(0,len(peopleNameList)-1)]
            personEntity.card1 = findCard()
            personEntity.card2 = findCard()

            peopleList.append(personEntity)

        # Use house to extract 3 more cards for play
        card3 = findCard()
        card4 = findCard()
        card5 = findCard()
        card6 = findCard()
        card7 = findCard()

        # Only start recording statistics as games progress past 16 Cards
        for x in peopleList:
            #print x.name, x.card1, x.card2, card3, card4, card5
            if(findBestCombination(x.card1, x.card2, card3, card4, card5, card6, card7) == "No Pair"):
                noPair += 1
            elif(findBestCombination(x.card1, x.card2, card3, card4, card5, card6, card7) == "Pair"):
                onePair += 1
            elif(findBestCombination(x.card1, x.card2, card3, card4, card5, card6, card7) == "Two Pair"):
                twoPair += 1
            elif(findBestCombination(x.card1, x.card2, card3, card4, card5, card6, card7) == "Three of a kind"):
                threeOfKind += 1
            elif(findBestCombination(x.card1, x.card2, card3, card4, card5, card6, card7) == "Full House"):
                fullHouse += 1
            elif(findBestCombination(x.card1, x.card2, card3, card4, card5, card6, card7) == "Four of a kind"):
                fourOfKind += 1
            else:
                print findBestCombination(x.card1, x.card2, card3, card4, card5, card6, card7)

        currentGame += 1
        # print "two Pairs", twoPair
        # print "Full house", fullHouse
        # print "Four of Kind", fourOfKind
        print "Completed Game: ", currentGame

    print "Players: ", numOfPlayers
    print "Games Played: ", numOfGamesToPlay
    print "Cards Reshuffled:", shuffledCardsCounter

    graphData = (noPair, onePair, twoPair, threeOfKind, fullHouse, fourOfKind)

    noPair1 = np.divide(noPair,float(sum(graphData)))*100
    onePair1 = np.divide(onePair,float(sum(graphData)))*100
    twoPair1 = np.divide(twoPair,float(sum(graphData)))*100
    threeOfKind1 = np.divide(threeOfKind,float(sum(graphData)))*100
    fullHouse1 = np.divide(fullHouse,float(sum(graphData)))*100
    fourOfKind1 = np.divide(fourOfKind,float(sum(graphData)))*100

    graphData1 = (noPair1*noPair/100, onePair1*onePair/100, twoPair1*twoPair/100, threeOfKind1*threeOfKind/100, fullHouse1*fullHouse/100, fourOfKind1*fourOfKind/100)

    print graphData
    print numOfGamesToPlay*(2*numOfPlayers+3)
    print numOfPlayers
    print graphData1

    plt.ioff()
    n_groups = 6
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35

    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, graphData, bar_width,
                 alpha=1,
                 color='b',
                 error_kw=error_config,
                 label='Dont talk')
    rects2 = plt.bar(index+bar_width, graphData1, bar_width,
                 alpha=1,
                 color='r',
                 error_kw=error_config,
                 label='Dont talk')

    plt.xlabel('Hands')
    plt.ylabel('Hands Dealt')
    plt.title('Poker Hands versus commonality')
    plt.xticks(index + (2*bar_width)/ 2, ('NP '+str(round(noPair1,2))+"%", 'P '+str(round(onePair1,2))+"%", '2P '+str(round(twoPair1,2))+"%", '3K '+str(round(threeOfKind1,2))+"%", 'FH '+str(round(fullHouse1,2))+"%", '4K '+str(round(fourOfKind1,2))+"%"))

    plt.tight_layout()
    plt.show()

    '''
    plt.ioff()
    # chr(65) = A -> chr(69) = D
    for x in range(numOfTries):
        currentCardValue = chr(random.randint(65,68)) + str(random.randint(1,13))
        playedcardList.append(currentCardValue)

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

'''


mainMethod()
