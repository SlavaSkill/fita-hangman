from gameplay.game import Game
import random 
from nltk import word_tokenize


with open('data/words.txt', 'r', encoding='utf-8') as file:
    words = file.read()
    words = word_tokenize(words)
    # words = list(words.split("\n"))
    # random.choice(word)
    # word = list(word)
    # word.pop()
    #words = file.read()
    #words = word_tokenize(words)
    #print(words)

# Randomizē spēles palaišanas brīdī (1x) - pietiekami
#random.shuffle(words)

while True:
    # Randomizē katrā spēlē
    random.shuffle(words)
    word = words.pop()
    game = Game(word)
    #game = Game(random.choice(words))
    game.play()
    
    exit_ = str(input('do you want to exit? y/n: '))
    if exit_ == 'y':
        break
    else:
        continue