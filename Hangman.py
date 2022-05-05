# Python program to illustrate Hangman Game:
import collections
import random as ra
# from collections import counter

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut 
watermelon cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
# print(someWords)

word = ra.choice(someWords)     # randomly choose a word from the list of someWords

# if __name__ = '__main__':

print("Guess the word! Hint: word is a name of a fruit")

for i in word:
  print("_", end=' ')
print()

playing = True
#    List for storing the letters guessed by the player

letterGuessed = ''
chance = len(word)+2
flag = 0
correct = 0

try:
  while(chance != 0) and flag == 0:
    print()
    chance -= 1

    try:
      guess = str(input('Enter a letter to guess: '))
    except:
      print("Enter only letter!")
      continue
    # Validation of the Guess:
    if not guess.isalpha():
     print("Enter only a Letter")
     continue
    elif len(guess) > 1:
      print('Enter only single Letter')
      continue
    elif guess in letterGuessed:
      print('You have already guessed this letter')
      continue

#     if letter is guessed correctly
    if guess in word:
      k = word.count(guess)    # k store the number of times the gussed word appear in the word
      for _ in range(k):
        letterGuessed += guess

#     print the word
    for char in word:
      if char in letterGuessed and (collections.Counter(letterGuessed) != collections.Counter(word)):
        print(char, end=' ')
        correct += 1

#               if the user has guessed all the letters
      elif collections.Counter(letterGuessed) == collections.Counter(word):
        print("The word is: ", end=' ')
        print(word)

        flag = 1
        print('..............................................................')
        print("Congratulation, You won!")
        print('.........................................................')

        break
        break

      else:
        print('_', end=' ')
  if chance <= 0 and (collections.Counter(letterGuessed)!=collections.Counter(word)):
    print()
    print("You lost! Try again....")
    print(f"The word was: ", word)
except keywordInterrupt:
  print()
  print('Bye! Try again.')

  exit()









