#!/usr/bin/python3
#---------------------------------------------------
#AUTHOR: jacobdahl09@gmail.com
#DATE CREATED: October 21, 2021 12:54pm
#DESCRIPTION: This code allows for you to play the popular "hacking" minigame from the Fallout franchise.
#---------------------------------------------------

#Necessary Imports
import random
import sys
import time
import os

os.system("color")
#Initializing for all of the variables used throughout the code
GARBAGE_CHARS = ['~','!','@','#','$','%','^','&','*',',','.','?','=',';',':'] #The random characters that help fill out the terminal
terminal = [] #Stores the terminal that needs to be printed each turn
tries_left = 5 #Number of tries left
player_input = "" #Stores the player's input
player_input_list = []
pickedwords = [] #Stores the chosen words from the text file
secret_word = "" #Stores the chosen secret word

#Opens the wordlist.txt file and stores its lines in 'WORDS'
with open('wordlist.txt') as wordlistfile:
    WORDS = wordlistfile.readlines()

#For loop that pulls each word out of each line
for i in range(len(WORDS)):
    WORDS[i] = WORDS[i].strip().upper()

#The main function that runs the other functions to play the game
def main():
    printstartscreen()
    clear_console()
    animate()
    pick_words()
    build_terminal()
    print_terminal()
    check_input()

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}

def printstartscreen():
    print(COLOR["GREEN"],"WELCOME TO PR1ME INDUSTRIES (TM) TERMLINK\n",COLOR["ENDC"])
    print(COLOR["GREEN"],"Initializing Pr1me Industries(TM) MF Boot Agent v2.3.0\n",COLOR["ENDC"])
    time.sleep(1.1)
    print(COLOR["GREEN"],"RETROS BIOS",COLOR["ENDC"])
    time.sleep(1.1)
    print(COLOR["GREEN"],"PBIOS-4.02.08.00 52EES.E7.E8\n",COLOR["ENDC"])
    time.sleep(1.1)
    print(COLOR["GREEN"],"Copyright 2019-2021 Pr1me Ind.",COLOR["ENDC"])
    print(COLOR["GREEN"],"Uppermem: 1024 KB",COLOR["ENDC"])
    print(COLOR["GREEN"],"Root (5A8)",COLOR["ENDC"])
    time.sleep(1.1)
    print(COLOR["GREEN"],"Maintenance Mode",COLOR["ENDC"])
    time.sleep(1.1)
    clear_console()
    print(COLOR["GREEN"], "\n\n\n\n                                          ***   ***   *********   *********", COLOR["ENDC"])
    print(COLOR["GREEN"], "                                         ***   ***   *********   ***      ", COLOR["ENDC"])
    print(COLOR["GREEN"], "                                         ***   ***   ***   ***   ******** ", COLOR["ENDC"])
    print(COLOR["GREEN"], "                                         ***   ***   ***   ***    ********", COLOR["ENDC"])
    print(COLOR["GREEN"], "                                         *********   *********         ***", COLOR["ENDC"])
    print(COLOR["GREEN"], "                                         *********   *********   *********", COLOR["ENDC"])
    print(COLOR["GREEN"], "                                                 PR1ME INDUSTRIES", COLOR["ENDC"])
    print(COLOR["GREEN"], "                                             UNIFIED OPERATING SYSTEM", COLOR["ENDC"])
    print(COLOR["GREEN"], "                                                Copyright 2019-2021\n\n\n                                               Press any key to start.", COLOR["ENDC"]) 
    input()

#This function simulates loading in python
def animate():
    timelength = random.randint(4, 6)
    for i in range(timelength):
        sys.stdout.write('\r\033[1;32;40mloading |')
        time.sleep(0.1)
        sys.stdout.write('\r\033[1;32;40mloading /')
        time.sleep(0.1)
        sys.stdout.write('\r\033[1;32;40mloading -')
        time.sleep(0.1)
        sys.stdout.write('\r\033[1;32;40mloading \\')
        time.sleep(0.1)

#This function picks 20 random words and stores them in the variable 'pickedwords'
def pick_words():
    global pickedwords
    global secret_word

    for i in range(21):
        tempval = random.randint(1, 444)
        chosenword = WORDS[tempval]
        pickedwords.append(chosenword)
    secret_word = random.choice(pickedwords)

#This function builds the terminal that will be printed
def build_terminal():
    global terminal
    word_countl = 0 #Left half word count
    word_countr = 10 #Right half word count


    clear_console()

    for i in range(10):#Creates 10 lines
        fvaluel = random.randint(100, 199)#Creates a value from 100 to 199
        fvalue2 = random.randint(200, 299)#Creates a value from 200 to 299
        randomcharsleft = (''.join(random.choice(GARBAGE_CHARS) for j in range(5)))#Puts 5 random characters in the left halve's lines
        randomcharsright = (''.join(random.choice(GARBAGE_CHARS) for j in range(5)))#Puts 5 random characters in the right halve's lines
        index = random.randint(0, 4)
        randomcharsleft = randomcharsleft[:index] + pickedwords[word_countl] + randomcharsleft[index:]#Stores a random word from the array 'pickedwords' in each line
        word_countl += 1
        
        index = random.randint(0, 4)
        randomcharsright = randomcharsright[:index] + pickedwords[word_countr] + randomcharsright[index:]
        word_countr += 1
        
        terminal.append('0xF' + str(fvaluel) + ' ' + randomcharsleft + ' ' + '0xF' + str(fvalue2) + ' ' + randomcharsright)

    terminal = '\n'.join(terminal)

#This function prints the terminal
def print_terminal():
    global terminal
    global tries_left

    print("\033[1;32;40mPR1ME INDUSTRIES (TM) TERMLINK PROTOCOL\nPASSWORD REQUIRED\n")
    print(str(tries_left) + "\033[1;32;40m ATTEMPT(S) LEFT: " + printasterisks(tries_left) + "\n")
    print(terminal)

#This function prints the correct number of asterisks
def printasterisks(triesleft):
    asterisks = "* " * triesleft
    return asterisks

#This function clears the console
def clear_console():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

#This function checks the player's input to see if it is correct or incorrect
def check_input():
    global player_input
    global player_input_list
    global secret_word
    global tries_left

    player_input = input("> ").upper()

    while(tries_left > 1):
        if(player_input == secret_word):
            clear_console()
            print_terminal()
            print(">" + player_input)
            print("\033[1;32;40mA C C E S S  G R A N T E D")
            input()
            exit()
        elif(player_input == "DEBUG_ANS"):
            print(secret_word)
            input()
            clear_console()
            print_terminal()
            update_input(secret_word, player_input)
        else:
            tries_left -= 1
            clear_console()
            print_terminal()
            print(">" + player_input)
            print(">Entry denied")
            update_input(secret_word, player_input)
    print("\033[1;31;40mA C C E S S  D E N I E D")
    input()
    exit()

#This function checks if the player's inputted string is the same as the secret word
def update_input(secret_word, player_input):
    correct_count = 0

    for i in range(len(secret_word)):#Loops through each letter of the secret word and the player's input
        if(secret_word[i] == player_input[i]): #If player's letter at index is the same as secre'ts, then return it
            correct_count += 1
    clear_console()
    print_terminal()
    print(player_input)
    print(">" + str(correct_count) + "/7 correct.")#Prints the correct amount as ">4/7 correct." As an example
    check_input()

#Runs the main function
if __name__ == "__main__":
    main()
