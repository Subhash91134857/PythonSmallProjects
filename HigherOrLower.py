# HigherOrLower
import random as ra


# Card constants

SUIT_TUPLE = ('Spades', 'Hearts', 'Club', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7',
               '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

# Pass in a deck and this function return a raandom card from thr deck


def getCard(deckListIn):
    thisCard = deckListIn.pop()  # pop one of the top of the deck and return
    return thisCard

# For shuffling the card


def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # make a copy of the starting deck
    ra.shuffle(deckListOut)
    return deckListOut

# Main code


print("Welcome to Higher or Lower.\n")
print("You have to choose whether the next card to be shown will be higher or lower than the current card.")
print("Getting it right add 20 points; get it wrong and you lose 15 points.\n")
print("You have 50 points to start.")
print('\n')

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue+1}
        startingDeckList.append(cardDict)
score = 50

# Play multiples game:
x=1
while True:
    print()
    gameDeckList=shuffle(startingDeckList)
    currentCardDict=getCard(gameDeckList)
    currentCardRank=currentCardDict['rank']
    currentCardValue=currentCardDict['value']
    currentCardSuit=currentCardDict['suit']
    print("Starting card is:",currentCardRank+' of '+currentCardSuit)
    print()
   
    for cardNumber in range(0,NCARDS):
        answer=input("Will the next card be higher or lower than the "+currentCardRank+" of "+currentCardSuit +" ? (Enter the h for higher or l for lower):" )
        answer=answer.casefold()

        nextCardDict=getCard(gameDeckList)
        nextCardRank=nextCardDict['rank']
        nextCardSuit=nextCardDict["suit"]
        nextCardValue=nextCardDict['value']
        print("Next card is: "+nextCardRank+" of "+nextCardSuit)

        if answer=='h':
             if nextCardValue>currentCardValue:
                print("You got it right, it was higher")
                score+=20
             else:
                print("Sorry! it was not higher")
                score-=15
        elif answer=="l":
            if nextCardValue<currentCardValue:
                score+=20
                print('You got it right, it was lower')
            else:
                score=score-15
                print("Sorry!, it was not lower")
        print("Your score is: ",score)
        print()
        currentCardRank=nextCardRank
        currentCardValue=nextCardValue
    goAgain=input("To play again, press enter, or 'q' to quit:") 
    if goAgain =='q':
            break 
print("ok bye")            
    
    
    