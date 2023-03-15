'''
Really simple hangman game using print and input
'''


import random
file = open('list_of_words.txt')
line = random.randint(1, 1000)
content = file.readlines()
word = content[line]
word = word.rstrip()
letters = []
guessed_letters = []
wrong_letters = []

#print(word)

for x in word:
 x.upper()
 letters.append(x)
for x in letters:
 guessed_letters.append('_')
print(''.join(guessed_letters))

def guessed(letter, word):
 letter_count = 0
 if letter == word:
  print("You have won, congratulations!")
  return False
 for x in letters:
  if letter is x:
   guessed_letters[letter_count] = letter
  letter_count = letter_count + 1
 if letter not in word:
   print("Letter not in word")
   print("You have", 4 - len(wrong_letters), "guesses remaining")
   wrong_letters.append(letter)

while True:
 guess = input("Enter guess: ")
 guess.upper()
 if guessed(guess, word) is False:
  break
 print(''.join(guessed_letters))
 if '_' not in guessed_letters:
  print("Congratulations! You have won!")
  break
 elif len(wrong_letters) == 5:
  print("You have hung your man")
  print("Word was: {}".format(word))
  break
