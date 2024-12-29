import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word = ['aya', 'apple', 'mazen', 'osasma']
random_word = random.choice(word)
display = ["_"] *len(random_word)
print(' '.join(display))
print(HANGMANPICS[0])
list_in = []
live = 6
while "_" in display and live > 0:
    guess = input('please guess the letter :\n').lower()
    if guess in list_in:
       print('you already guessed this letter')
       continue
    list_in.append(guess)
       
    if guess not in random_word:
        live -= 1
        print(HANGMANPICS[6-live])
    else:
       for position in range(len(random_word)):
           if random_word[position] == guess:
             display[position] = guess
    print(display)
    print(f'you have {live}')
if live == 0:
   print(HANGMANPICS[-1])







