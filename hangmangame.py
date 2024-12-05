import random
def print_design(guesses,word):
    #hangman visual after each guess that is wrong
    if (guesses == 0):
        print("__________\n"
              "|     |\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|__________\n")
    elif(guesses == 1):
        print("__________\n"
              "|     |\n"
              "|     O\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|__________\n")
    elif(guesses == 2):
        print("__________\n"
              "|     |\n"
              "|     O\n"
              "|     |\n"
              "|\n"
              "|\n"
              "|\n"
              "|__________\n")
    elif(guesses == 3):
        print("__________\n"
              "|     |\n"
              "|     O\n"
              "|     |\n"
              "|     |\n"
              "|\n"
              "|\n"
              "|__________\n")
    elif(guesses == 4):
        print("__________\n"
              "|     |\n"
              "|     O\n"
              "|     |\n"
              "|     |\n"
              "|    /\n"
              "|\n"
              "|__________\n")
    elif(guesses == 5):
        print("__________\n"
              "|     |\n"
              "|     O\n"
              "|    \\|/\n"
              "|     |\n"
              "|    / \\ \n"
              "|\n"
              "|__________\n")
    elif(guesses == 6):
        print("__________\n"
              "|     |\n"
              "|     O\n"
              "|    \\|/\n"
              "|     |\n"
              "|    / \\ \n"
              "|\n"
              "|__________\n")
        print("\n")
        print("The word is %s. \n" % word)
        print("\nYOU LOST! TRY AGAIN!")
        print("\nDo you like to play again? Type 1 for yes or 2 for no:")
        again = input("> ")
        again = again.lower()
        if again == "1":
            hangman()
        return

#getting the random word from the other file
def randomword():
    file = open("COMP")
    words = file.readlines()
    myword = random.choice(words)
    myword = str(myword).strip("")
    myword = str(myword).strip("''")
    myword = str(myword).strip("\n")
    myword = str(myword).strip("\r")
    myword = myword.lower()
    return myword

def hangman():
    guesses = 0
    word = randomword()
    wordlist = list(word)
    blanks = "_" * len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_lists = []
    print("Let's play Hangman!\n")
    print_design(guesses,word)
    print("\n"+''.join(blanks_list)) #row of dashes
    print("Guess a letter:")
    while guesses < 6:
        guess = input("> ")
        guess = guess.lower()

        #if the player enters more than one letter at a time
        if len(guess)>1:
            print("Please enter one letter at a time!")

        #if the player hits enter without entering a letter
        elif guess == "":
            print("Enter a letter")

        #if the player repeats the letter that has already been guessed, then display the list of guessed letters
        elif guess in guess_lists:
            print("Already guessed! Here is what you have guessed:")
            print(' '.join(guess_lists))

        #if all of the above conditions fail, use an else block to append the guessed letter to the list of guessed letters
        else:
            guess_lists.append(guess)
            i = 0
            while i<len(word):
                if guess == word[i]: #if the guessed letter is in the given word
                    new_blanks_list[i] = wordlist[i]
                i = i+1

            #if the guessed letter is wrong, ask the user to guess again
            if new_blanks_list == blanks_list:
                    print("Incorect. Guess again.")
                    guesses = guesses+1
                    print_design(guesses,word)

            #if the guessed letter is correct, insert the letter in the correct postition
            elif wordlist!= blanks_list:
                blanks_list = new_blanks_list[:]
                print(''.join(blanks_list))

                #finally, if the whole word is guessed correctly, the player wins
                if wordlist == blanks_list:
                    print("\nYOU WIN!!!!\n")
                    print("Do you want to play again? If so press 1 for yes and 2 for no.")
                    again = input("> ")
                    if again == "yes":
                        hangman()
                    quit()                
                
                #or if only the guessed letter is correct, ask the user to guess the next word
                else:
                 print("Great guess! Guess the next letter!")
hangman()