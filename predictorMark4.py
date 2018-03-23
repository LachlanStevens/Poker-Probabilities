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
Ok So we want to find out how often does someone dealt a ace,10, jack, queen or king win
'''
'''
Cards dealt per round = 2 per player, per game + 3 for house per game
 = (2*numOfPlayers)* numOfGames + 3*numOfGames
 = ((numOfGames)*(2*numOfPlayers + 3))
'''


numOfPlayers = 8
numOfDecks = 1
numOfGamesToPlay = 500

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

def findBestCombination(card1, card2, card3, card4, card5):
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
    # card6 = card6[1:]
    # card7 = card7[1:]

    activeList = [card1, card2, card3, card4, card5]
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

    winsWithA10JQK = 0
    winsWith2A10JQK = 0

    winningCardsList = []
    while(currentGame < numOfGamesToPlay):
        # Begin by defining game players
        for x in range(numOfPlayers):
            personEntity = person()
            personEntity.name = peopleNameList[random.randint(0,len(peopleNameList)-1)]
            personEntity.card1 = findCard()
            personEntity.card2 = findCard()

            peopleList.append(personEntity)

        # Use house to extract 5 more cards for play
        card3 = findCard()
        card4 = findCard()
        card5 = findCard()
        card6 = findCard()
        card7 = findCard()

        # Only start recording statistics as games progress past 16 Cards
        winner = ""
        bestCombinationNumber = 0
        for x in peopleList:
            #print x.name, x.card1, x.card2, card3, card4, card5
            bestCombination = findBestCombination(x.card1, x.card2, card3, card4, card5)
            if(bestCombination == "No Pair"):
                #noPair += 1
                if(bestCombinationNumber <= 0):
                    bestCombinationNumber = 0
                    winner = x.name, ":", bestCombination, x.card1, x.card2
            elif(bestCombination == "Pair"):
                #onePair += 1
                if(bestCombinationNumber <= 1):
                    bestCombinationNumber = 1
                    winner = x.name, bestCombination, x.card1, x.card2
            elif(bestCombination == "Two Pair"):
                #twoPair += 1
                if(bestCombinationNumber <= 2):
                    bestCombinationNumber = 2
                    winner = x.name, bestCombination, x.card1, x.card2
            elif(bestCombination == "Three of a kind"):
                #threeOfKind += 1
                if(bestCombinationNumber <= 3):
                    bestCombinationNumber = 3
                    winner = x.name, bestCombination, x.card1, x.card2
            elif(bestCombination == "Full House"):
                #fullHouse += 1
                if(bestCombinationNumber <= 4):
                    bestCombinationNumber = 4
                    winner = x.name, bestCombination, x.card1, x.card2
            elif(bestCombination == "Four of a kind"):
                #fourOfKind += 1
                if(bestCombinationNumber <= 5):
                    bestCombinationNumber = 5
                    winner = x.name, bestCombination, x.card1, x.card2
            else:
                print bestCombination
                print "ERRROR"

        currentGame += 1
        # print "two Pairs", twoPair
        # print "Full house", fullHouse
        # print "Four of Kind", fourOfKind
        print "Completed Game: ", currentGame
        #print winner[0] + " won with a " + winner[1]
        card1 = x.card1[1:]
        card2 = x.card2[1:]
        if(winner[1] == "No Pair"):
            noPair += 1
            print winner[1]
        elif(winner[1] == "Pair"):
            onePair += 1
            print winner[1]
        elif(winner[1] == "Two Pair"):
            twoPair += 1
            print winner[1]
        elif(winner[1] == "Three of a kind"):
            threeOfKind += 1
            winningCardsList.append([card1,card2])
        elif(winner[1] == "Full House"):
            fullHouse += 1
            print winner[1]
        elif(winner[1] == "Four of a kind"):
            fourOfKind += 1
            print winner[1]
        else:
            print winner[1]
            print "ERroror"
        if((int(str(winner[2])[1:]) == 10) or (int(str(winner[2])[1:]) >= 20)):
            winsWithA10JQK += 1
            if((int(str(winner[3])[1:]) == 10) or (int(str(winner[3])[1:]) >= 20)):
                winsWith2A10JQK += 1
                winsWithA10JQK -= 1
    print "Players: ", numOfPlayers
    print "Games Played: ", numOfGamesToPlay
    print "Cards Reshuffled:", shuffledCardsCounter
    
    repeatedList = []
    repeatedList1 = []
    repeatedList2 = []
    repeatedList3 = []
    repeatedList4 = []
    repeatedList5 = []
    repeatedList6 = []
    repeatedList7 = []
    repeatedList8 = []
    repeatedList9 = []
    repeatedList10 = []
    repeatedList11 = []
    repeatedList12 = []
    repeatedList13 = []

    lossWithA10JQK = 0
    winsWithA10JQK = 0
    winsWith2A10JQK = 0

    for cards in winningCardsList:
        # if((cards in repeatedList) or (cards[::-1] in repeatedList)):
        #     if((cards in repeatedList1) or (cards[::-1] in repeatedList1)):
        #         if((cards in repeatedList2) or (cards[::-1] in repeatedList2)):
        #             if((cards in repeatedList3) or (cards[::-1] in repeatedList3)):
        #                 if((cards in repeatedList4) or (cards[::-1] in repeatedList4)):
        #                     if((cards in repeatedList5) or (cards[::-1] in repeatedList5)):
        #                         if((cards in repeatedList6) or (cards[::-1] in repeatedList6)):
        #                             if((cards in repeatedList7) or (cards[::-1] in repeatedList7)):
        #                                 if((cards in repeatedList8) or (cards[::-1] in repeatedList8)):
        #                                     if((cards in repeatedList9) or (cards[::-1] in repeatedList9)):
        #                                         if((cards in repeatedList10) or (cards[::-1] in repeatedList10)):
        #                                             if((cards in repeatedList11) or (cards[::-1] in repeatedList11)):
        #                                                 if((cards in repeatedList12) or (cards[::-1] in repeatedList12)):
        #                                                     if((cards in repeatedList13) or (cards[::-1] in repeatedList13)):
        #                                                         print "13 DUPLICATES:O"
        #                                                     else:
        #                                                         repeatedList13.append(cards)
        #                                                 else:
        #                                                     repeatedList12.append(cards)
        #                                             else:
        #                                                 repeatedList11.append(cards)
        #                                         else:
        #                                             repeatedList10.append(cards)
        #                                     else:
        #                                         repeatedList9.append(cards)
        #                                 else:
        #                                     repeatedList8.append(cards)
        #                             else:
        #                                 repeatedList7.append(cards)
        #                         else:
        #                             repeatedList6.append(cards)
        #                     else:
        #                         repeatedList5.append(cards)
        #                 else:
        #                     repeatedList4.append(cards)
        #             else:
        #                 repeatedList3.append(cards)
        #         else:
        #             repeatedList2.append(cards)
        #     else:
        #         repeatedList1.append(cards)
        # else:
        #     repeatedList.append(cards)
        print cards
        print cards[0]
        print cards[1]
        if((int(cards[0]) == 10) or (int(cards[0]) >= 20)):
            winsWithA10JQK += 1
            if((int(cards[1]) == 10) or (int(cards[1]) >= 20)):
                winsWith2A10JQK += 1
                winsWithA10JQK -= 1
                print cards[0]
        else:
            if((int(cards[1]) == 10) or (int(cards[1]) >= 20)):
                winsWithA10JQK += 1
            else:
                lossWithA10JQK += 1



    #print collections.Counter(winningCardsList).most_common(3)
    # if(len(repeatedList13) > 0):
    #     print "list 13"
    #     for item in repeatedList13:
    #         for card in item:
    #             if((int(card) == 10) or (int(card) >= 20)):
    #                 winsWithA10JQK += 1
    #                 if((int(card) == 10) or (int(card) >= 20)):
    #                     winsWith2A10JQK += 1
    #                     winsWithA10JQK -= 1
    #             else:
    #                 lossWithA10JQK += 1
    # else:
    #     if(len(repeatedList12) > 0):
    #         print "list 12"
    #         for item in repeatedList12:
    #             for card in item:
    #                 if((int(card) == 10) or (int(card) >= 20)):
    #                     winsWithA10JQK += 1
    #                     if((int(card) == 10) or (int(card) >= 20)):
    #                         winsWith2A10JQK += 1
    #                         winsWithA10JQK -= 1
    #                 else:
    #                     lossWithA10JQK += 1
    #     else:
    #         if(len(repeatedList11) > 0):
    #             print "list 11"
    #             for item in repeatedList11:
    #                 for card in item:
    #                     if((int(card) == 10) or (int(card) >= 20)):
    #                         winsWithA10JQK += 1
    #                         if((int(card) == 10) or (int(card) >= 20)):
    #                             winsWith2A10JQK += 1
    #                             winsWithA10JQK -= 1
    #                     else:
    #                         lossWithA10JQK += 1
    #         else:
    #             if(len(repeatedList10) > 0):
    #                 print "list 10"
    #                 for item in repeatedList10:
    #                     for card in item:
    #                         if((int(card) == 10) or (int(card) >= 20)):
    #                             winsWithA10JQK += 1
    #                             if((int(card) == 10) or (int(card) >= 20)):
    #                                 winsWith2A10JQK += 1
    #                                 winsWithA10JQK -= 1
    #                         else:
    #                             lossWithA10JQK += 1
    #             else:
    #                 if(len(repeatedList9) > 0):
    #                     print "list 9"
    #                     for item in repeatedList9:
    #                         for card in item:
    #                             if((int(card) == 10) or (int(card) >= 20)):
    #                                 winsWithA10JQK += 1
    #                                 if((int(card) == 10) or (int(card) >= 20)):
    #                                     winsWith2A10JQK += 1
    #                                     winsWithA10JQK -= 1
    #                             else:
    #                                 lossWithA10JQK += 1
    #                 else:
    #                     if(len(repeatedList8) > 0):
    #                         print "list 8"
    #                         for item in repeatedList8:
    #                             for card in item:
    #                                 if((int(card) == 10) or (int(card) >= 20)):
    #                                     winsWithA10JQK += 1
    #                                     if((int(card) == 10) or (int(card) >= 20)):
    #                                         winsWith2A10JQK += 1
    #                                         winsWithA10JQK -= 1
    #                                 else:
    #                                     lossWithA10JQK += 1
    #                     else:
    #                         if(len(repeatedList7) > 0):
    #                             print "list 7"
    #                             for item in repeatedList7:
    #                                 for card in item:
    #                                     if((int(card) == 10) or (int(card) >= 20)):
    #                                         winsWithA10JQK += 1
    #                                         if((int(card) == 10) or (int(card) >= 20)):
    #                                             winsWith2A10JQK += 1
    #                                             winsWithA10JQK -= 1
    #                                     else:
    #                                         lossWithA10JQK += 1
    #                         else:
    #                             if(len(repeatedList6) > 0):
    #                                 print "list 6"
    #                                 for item in repeatedList6:
    #                                     for card in item:
    #                                         if((int(card) == 10) or (int(card) >= 20)):
    #                                             winsWithA10JQK += 1
    #                                             if((int(card) == 10) or (int(card) >= 20)):
    #                                                 winsWith2A10JQK += 1
    #                                                 winsWithA10JQK -= 1
    #                                         else:
    #                                             lossWithA10JQK += 1
    #                             else:
    #                                 if(len(repeatedList5) > 0):
    #                                     print "list 5"
    #                                     for item in repeatedList5:
    #                                         for card in item:
    #                                             if((int(card) == 10) or (int(card) >= 20)):
    #                                                 winsWithA10JQK += 1
    #                                                 if((int(card) == 10) or (int(card) >= 20)):
    #                                                     winsWith2A10JQK += 1
    #                                                     winsWithA10JQK -= 1
    #                                             else:
    #                                                 lossWithA10JQK += 1
    #                                 else:
    #                                     if(len(repeatedList4) > 0):
    #                                         print "list 4"
    #                                         for item in repeatedList4:
    #                                             for card in item:
    #                                                 if((int(card) == 10) or (int(card) >= 20)):
    #                                                     winsWithA10JQK += 1
    #                                                     if((int(card) == 10) or (int(card) >= 20)):
    #                                                         winsWith2A10JQK += 1
    #                                                         winsWithA10JQK -= 1
    #                                                 else:
    #                                                     lossWithA10JQK += 1
    #                                     else:
    #                                         if(len(repeatedList3) > 0):
    #                                             print "list 3"
    #                                             for item in repeatedList3:
    #                                                 for card in item:
    #                                                     if((int(card) == 10) or (int(card) >= 20)):
    #                                                         winsWithA10JQK += 1
    #                                                         if((int(card) == 10) or (int(card) >= 20)):
    #                                                             winsWith2A10JQK += 1
    #                                                             winsWithA10JQK -= 1
    #                                                     else:
    #                                                         lossWithA10JQK += 1
    #                                         else:
    #                                             if(len(repeatedList2) > 0):
    #                                                 print "list 2"
    #                                                 for item in repeatedList2:
    #                                                     for card in item:
    #                                                         if((int(card) == 10) or (int(card) >= 20)):
    #                                                             winsWithA10JQK += 1
    #                                                             if((int(card) == 10) or (int(card) >= 20)):
    #                                                                 winsWith2A10JQK += 1
    #                                                                 winsWithA10JQK -= 1
    #                                                         else:
    #                                                             lossWithA10JQK += 1
    #                                             else:
    #                                                 if(len(repeatedList1) > 0):
    #                                                     print "list 1"
    #                                                     for item in repeatedList1:
    #                                                         for card in item:
    #                                                             if((int(card) == 10) or (int(card) >= 20)):
    #                                                                 winsWithA10JQK += 1
    #                                                                 if((int(card) == 10) or (int(card) >= 20)):
    #                                                                     winsWith2A10JQK += 1
    #                                                                     winsWithA10JQK -= 1
    #                                                             else:
    #                                                                 lossWithA10JQK += 1
    #                                                 else:
    #                                                     if(len(repeatedList) > 0):
    #                                                         print "list 0"
    #                                                         for item in repeatedList:
    #                                                             for card in item:
    #                                                                 if((int(card) == 10) or (int(card) >= 20)):
    #                                                                     winsWithA10JQK += 1
    #                                                                     if((int(card) == 10) or (int(card) >= 20)):
    #                                                                         winsWith2A10JQK += 1
    #                                                                         winsWithA10JQK -= 1
    #                                                                 else:
    #                                                                     lossWithA10JQK += 1
    #                                                     else:
    #                                                         print "Error"


    graphData = (winsWithA10JQK, winsWith2A10JQK, lossWithA10JQK)

    winsWithA10JQK1 = np.divide(winsWithA10JQK,float(sum(graphData)))*100
    winsWith2A10JQK1 = np.divide(winsWith2A10JQK,float(sum(graphData)))*100
    lossWithA10JQK1 = np.divide(lossWithA10JQK,float(sum(graphData)))*100

    graphData1 = (winsWithA10JQK1*sum(graphData)/100, winsWith2A10JQK1*sum(graphData)/100, lossWithA10JQK1*sum(graphData)/100)


    print graphData
    print numOfGamesToPlay*(2*numOfPlayers+3)
    print numOfPlayers
    print graphData1

    plt.ioff()
    n_groups = 3
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

    plt.xlabel('Games')
    plt.ylabel('Win vs. Loss of game')
    plt.title('Amount of wins versus losses when starting with an Ace, 10, Jack, Queen or King')
    plt.xticks(index + (2*bar_width)/ 2, ('Wins 1AJQK: '+str(round(winsWithA10JQK1,2))+"%", 'Wins: 2AJQK'+str(round(winsWith2A10JQK1,2))+"%", 'Loss: '+str(round(lossWithA10JQK1,2))+"%"))

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
