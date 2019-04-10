import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = str.split(line)
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()

def hangman():
    load_words()
    word = choose_word(wordlist)
    #print ('Hidded word is: ', word)
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word ', len(word), ' letters long')
    print ('Available letters: ', string.ascii_lowercase)
    display_word = '-'
    for n in range (1,len(word)):
        display_word = display_word + '-'
    #print (display_word)    
    alphabet = string.ascii_lowercase
    number_guess = 0
    while display_word != word:
        guess = input(str('Please guess a letter or a word: '))
        #alphabet = alphabet
        if len(guess) > 1:
            if guess == word:
                display_word = word
                #print('Great job! You won!')
                break
            else:
                print('Oops! You lost!', 'The word was: ', word)
                break    
        else:
            for i in alphabet:
                if i == guess:
                    alphabet = alphabet.replace(i,'')
                    for i in range(0,len(word)):
                        if word[i] == guess:
                            display_list = list(display_word)
                            display_list[i] = guess
                            display_word = ''
                            display_word = display_word.join(display_list) 
                        if guess not in word:
                            print('Oops! That letter is not in my word! Try again! ')
                            print('What you have so far: ', display_word)
                            print('-------------------------------------------------')
                            number_guess +=1
                            break   
                    if guess in word:
                        print ('Good guess: ', display_word)
                        print('-------------------------------------------------')
                    break
                if guess not in alphabet:
                    print ('You already guessed this letter!')
                    print('-------------------------------------------------')
                    break
            print('Available letters are: ', alphabet)
            print('You have ', len(word) + 2 - number_guess, 'guesses left')
        if number_guess >= (len(word) + 2):
            print ('Sorry, you lost!', 'The word was: ', word)
            break
    if display_word == word:
        print('Great job! You won!')

hangman()




