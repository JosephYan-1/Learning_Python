# ---
#    |
#    |
#   \O/
#    |
#   / \ == 6 tries, once i get strings started i will implement a hangman function

hangman_visual = [
    "---",      # 0 
    "  |",      # 1
    "  |",      # 2
    "   ",     # 3
    "   ",      # 4
    "   ",     # 5
]

def mistake(count):
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

def print_hangman():
    for element in hangman_visual:
        print(element)

# print_hangman()
# for i in range(7):
#     mistake(i) #this prints full hangman
# print_hangman()