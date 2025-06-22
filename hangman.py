# ---
#    |
#    |
#   \O/
#    |
#   / \ == 6 tries, once i get strings started i will implement a hangman function
from hangman_list import words
import random



def get_word():
    ran_gen = random.SystemRandom() #this uses system properties for better random numbers
    random_num = ran_gen.randint(0,49)

    return words[random_num]

def mistake(count, hangman_visual):
    match count:
        case 1:
            hangman_visual[3] = "  O"
        case 2:
            hangman_visual[3] = " \\O"
        case 3: 
            hangman_visual[3] += "/"
        case 4: 
            hangman_visual[4] = "  |"
        case 5:
            hangman_visual[5] = " /"
        case 6: 
            hangman_visual[5] += " \\"
    
    print(f"NOT FOUND, Mistake: {count}\n Tries left: {6-count}")

def print_hangman(hangman_visual):
    for element in hangman_visual:
        print(element)

def search_string(word, displayString, guess):
    found = 0
    newstring = ""
    for i in range (len(word)):
        if word[i] == guess:
            found += 1
            newstring = displayString[:i] + guess + displayString[i + 1:]
            displayString = newstring
        
    if found == 0:
        #did not find match
        return False, displayString

    return True, displayString

def playing(word):
    hangman_visual = [
    "---",      # 0 
    "  |",      # 1
    "  |",      # 2
    "   ",     # 3
    "   ",      # 4
    "   ",     # 5
    ]
    guessedLet = []
    count = 0
    WL = 0 #win/lose return 1 = win return 0 = lose
    displayString = "_" * len(word)
    print_hangman(hangman_visual)
    while (count != 6 and WL == 0):
        if displayString == word:
            WL = 1
            continue
        print(f"Guessed letters: {guessedLet}")
        print(f"{displayString} : {len(word)} letters")


        guess = input("Guess: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Only 1 letter at a time and no numbers") #some checks 
            continue
        if guess in guessedLet:
            print(f"ALREADY GUESSED: {guess}")
            continue

        guessedLet.append(guess) #add to list 

        found, displayString = search_string(word, displayString, guess)
        if found == 0:
            count += 1
            mistake(count, hangman_visual)
            print_hangman(hangman_visual)

    return WL , displayString

def main():
    print("LOADING HANGMAN")
    choice = input("READY TO PLAY? y/n: ").lower()
    while choice not in ("y", "n"):
        choice = input("MUST BE y/n: ").lower()

    while (choice == "y"):
        word = get_word()
        WL , displayString = playing(word)
        if WL == 0 :
            print("YOU LOSE")
        else: 
            print("YOU WON")

        print(f"You guessed: {displayString}, the word was {word}")
        
        
        choice = input("PLAY AGAIN? y/n: ").lower()
        while choice not in ("y", "n"):
            choice = input("PLAY AGAIN? y/n: ").lower()

    print("THANKS FOR PLAYING")

main()
# print_hangman()
# for i in range(7):
#     mistake(i) #this prints full hangman
# print_hangman()