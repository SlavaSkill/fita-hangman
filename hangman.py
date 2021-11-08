from os import name
from gameplay.game import Game

from scripts.split_difficulty import Dificulty

import random 
from nltk import word_tokenize
if_new_words = Dificulty(words_all=1)
if_new_words.diff()





while True:
    difficulty_info = 'Hello! There are 3 difficulty levels:"\n"1st - vārdi bez garumzīmēm un mīkstinājumiem"\n"2nd - ar garumzīmēm un mīkstinājumiem and more than 6 letters"\n"3rd - ar garumzīmēm un mīkstinājumiem and less than 6 letters'
    ## ievadi varbūt vajag while ciklā -> atkārtoti prasa ievadi, kamēr izvēlas 1 no trim
    print(difficulty_info)
    difficulty = input("Please, chose your game difficulty level (easy/medium/hard) : ")

    if difficulty == 'easy':
        with open('fita-hangman/data/easy_words.txt', 'r', encoding='utf-8') as file:
            file_contents = file.read()
            break
    elif difficulty == 'medium':
        with open('fita-hangman/data/medium_words.txt', 'r', encoding='utf-8') as file:
            file_contents = file.read()
            break
    elif difficulty == 'hard':
        with open('fita-hangman/data/hard_words.txt', 'r', encoding='utf-8') as file:
            file_contents = file.read()
            break
    else:
        print("Invalid input!")

# with open('data/words.txt', 'r', encoding='utf-8') as file:
#     file_contents = file.read()
    
    # for i in file_contents:
    #     if i is not '\n': print(i)
    
    # words = word_tokenize(words)
    # words = list(file_contents.split("\n"))

words = list(file_contents.split("', '"))
   
    # random.choice(word)
    # word = list(word)monta
    
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
