import random #Randomizes the words in the given categories

#Main Menu
def menu_choice():
    print("WELCOME TO WORDLE!\n\nRules:\n\nEach guess must be a valid five or seven-letter word.\nYour input must be in UPPERCASE LETTER only.\nIf the tile 🟩, the letter is in the correct spot.\nIf the tile 🟨, the letter is in the word, but it is not in the correct spot.\nIf the tile 🟥, the letter is not in the word. \n")
    print("1. Play\n2. Exit")

    user_input = int(input("\nHello there! Please choose an option: "))
    while user_input < 1 or user_input > 2:
    	print("Invalid input. Try Again.")
    	user_input = int(input("\nHello there! Please choose an option: "))
    if user_input == 1:
        choice_wordle()
    elif user_input == 2:
        print("Thanks for playing. Goodbye!")

#Wordle Menu
def choice_wordle():

    print("\nSelect your category:\n1. Countries\n2. Animals\n3. Colors\n")
    
    #Ensures that the user input is valid when choosing a category
    try:
        category_input = int(input("Enter the category number: "))
        while category_input < 1 or category_input > 3:
            print("Invalid category selection. Please choose a valid category.")
            category_input = int(input("Enter the category number: "))
        
        game_wordle(category_input - 1)
    except ValueError:
        print("Invalid input. Please enter a number.")
        choice_wordle()

#Wordle Game
def game_wordle(category):
    #Given words per category
    country = ["japan", "italy", "morocco", "finland", "egypt", "pakistan", "vietnam"]
    animal = ["vulture", "tiger", "eagle", "lizard", "shark", "giraffe", "turtle"]
    color = ["yellow", "black", "white", "violet", "orange", "fuchsia", "maroon"]

    list_of_categories = ["COUNTRIES", "ANIMALS", "COLORS"]
    categories = [country, animal, color]

    chosen_category = categories[category]
    secret_word = random.choice(chosen_category)  # Randomly selects a word
    
    #Displays the chosen category and the length of the word to be guessed by the user
    print("Category:", list_of_categories[category], "\n")
    print("     ", "_ " * len(secret_word), " \n")
   
   #Maximum attempts of the user for guessing the word
    max_attempts = 5
    attempts = 0
    
    #Ensures that the user inputs are letters and equal to the length of the secret word
    while attempts < max_attempts:
        user_guess = input("Enter a word: ").strip().upper()
        
        if not user_guess.isalpha():
            print("Invalid Input. Please enter only letters. \n")
            continue
        
        if len(user_guess) != len(secret_word):
            print(f"Invalid Input. Please input a {len(secret_word)}-LETTER word only.")
            continue
        
        verify = []
        feedback = []

        for i in range(len(secret_word)):
            if user_guess[i] == secret_word[i].upper():
                verify.append("🟩")
                feedback.append(user_guess[i])
            elif user_guess[i] in secret_word.upper():
                verify.append("🟨")
                feedback.append("_")
            else:
                verify.append("🟥")
                feedback.append("_")

        attempts += 1
        print(verify)
        print(feedback)

        if user_guess == secret_word.upper():
            print("Correct! You have guessed the word.")
            break
        elif attempts == max_attempts:
            print("Game over. The correct word is", secret_word, ".")

    continue_choice = input("\nWould you like to continue playing? (YES/NO): ").strip().upper()
    if continue_choice == "YES":
    	choice_wordle()
    elif continue_choice == "NO":
        print("Thanks for playing. Goodbye!")
    else:
    	print("\nInvalid input. Proceed to Menu.\n")
    	menu_choice()
   
 
menu_choice()
