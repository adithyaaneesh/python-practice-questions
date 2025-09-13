#5. Design a Word Guessing (Hangman) game using a word list.

import random
def options():
    words=['python','java','react','javascript','django','flutter']
    return random.choice(words)
def display_word(word,guess_letter):
    display=""
    for letter in word:
        if letter in guess_letter:
            display+=letter
        else:
            display+=' _ '
    return display
def hangman():
    word=options()
    guess_letter=[]
    attempts=6
    print('Welcome to Hangman')
    print('you have 6 attempts try to guess the word !')
    while attempts>0:
        print('\n',display_word(word,guess_letter))
        guess=input('enter the letter: ').lower()
        if guess in guess_letter:
            print('OOPS!, you have already guess this word')
        elif guess in word:
            print('correct guess')
            guess_letter.append(guess)
            if display_word(word,guess_letter)==word:
                print('CONGRATULATION,you win the word is: ',word)
                break
        else:
            print('incorrect guess')
            attempts-=1
            print('you have',attempts,'attempts')
    else:
        print('sorry you have no attempt,the word is:',word)
hangman()