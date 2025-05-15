
#create wordlist for later use in hangman game from words.txt file
def create_wordlist():
    wordlist = []
    with open("words.txt", "r") as file:
        words = file.read().split("\n")
        for word in words:
            wordlist.append(word)
    return wordlist

def test_action(x,y):
    z = x+y
    return z

#hangman ASCII art for use in game
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