import sys
from PhraseBank import *

def replace_by_stars(phrase,char):
     new_string = ""
     char = "A"
     for i in range(len(phrase)):
        if phrase[i] == char:
            new_string += char
        elif phrase[i] == " ":
            new_string += " "
        else:
            new_string += "*"
     return new_string[:-1]
def replace_char(star_phrase,phrase,user_input):
    star_list = list(star_phrase)
    for i in range(len(star_phrase)):
        if phrase[i] == user_input:
            star_list[i] = phrase[i]
    output = "".join(star_list)
    return output

def update_rem_letters(input, remaining_letters):
    if input == "":
        return remaining_letters
    letter_list = list(remaining_letters)
    final_list = []
    if input in remaining_letters:
        letter_list.pop(letter_list.index(input))
        for i in range(len(letter_list)):
            if not letter_list[i] == " " and not letter_list == input:
                final_list.append(letter_list[i])
        final_letters = " ".join(final_list)
        return final_letters

def play_one_round(phrase,remaining_letters):
            counter = 0
            star_phrase = ""
            for i in range(len(phrase)):
                if phrase[i] == " ":
                    star_phrase += " "
                elif phrase[i].isalpha():
                    star_phrase += "*"
            new_string = ""
            while counter < 5:
                print(f"The current phrase is  {star_phrase}")
                print(f"The letters you have not guessed yet are:")
                print(remaining_letters)
                user_input = str(input("Enter your next guess: ")).strip().upper()
                while user_input not in remaining_letters and len(user_input)>0:
                    print("Invalid letter choice! Pick from the letters shown:" + remaining_letters)
                    user_input = str(input("Enter your next guess: ")).strip().upper()
                remaining_letters = update_rem_letters(user_input, remaining_letters)
                print("\nYou guessed "+ user_input)

                if user_input in phrase:
                        print("This is present in the secret phrase")
                        new_string = replace_char(star_phrase,phrase,user_input)
                        star_phrase = new_string          
                else:
                        print("That is not in secret phrase.")
                        counter+=1
                if star_phrase == phrase:
                        print(f"The phrase is {phrase}")
                        print("YOU WIN!!!")
                        break
                print(f"You've made " + str(counter) + " wrong guess\n")
            if counter == 5:
                print(f"You lose. The secret phrase was {phrase}")

def main():
    fname = sys.argv[1]
    flag = 0
    print("This program plays the game of hangman.\nThe computer will pick a random phrase.\nAfter 5 wrong guesses you loses.\n")
    while flag == 0:
        p1 = PhraseBank(fname)
        remaining_letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
        print("Please choose a topic")
        print(f"      (0) MOVIE")
        print(f"      (1) COUNTRY NAME")
        print(f"      (2) NBA TEAM")
        try:
            user_input = int(input("\nEnter topic number (0,1,....): "))
        except ValueError:
            print("\nInvalid input!Please try again(0-2)!")
            user_input = int(input("\nEnter topic number (0,1,....): "))

        while user_input>2:
                print("\nInvalid choice! Please enter correct value(0-2)")
                user_input = int(input("\nEnter topic number (0,1,....): "))
        if user_input == 0:
            print("\nI am thinking of a MOVIE ...\n")
            phrase = str(p1.next_phrase("MOVIE")).strip()
            play_one_round(phrase,remaining_letters)

        if user_input == 1:
                print("\nI'm thinking of a country name...\n")
                phrase = str(p1.next_phrase("COUNTRY NAME")).strip()
                play_one_round(phrase,remaining_letters)

        if user_input == 2:
                print("\nI'm thinking of an NBA Team\n")
                phrase = str(p1.next_phrase("NBA TEAM")).strip()
                play_one_round(phrase,remaining_letters)

        user_choice = str(input("Do you want to play again(y/n): ")).strip().upper()
        while not (user_choice == "Y" or user_choice == "N"):
            print("\nInvalid choice! Please try again(y/n)\n")
            user_choice = str(input("Do you want to play again(y/n): ")).strip.upper()

        if user_choice == "Y":
                flag = 0
        elif user_choice == "N":
                flag = 1
                break

if __name__ == "__main__":
    main()
