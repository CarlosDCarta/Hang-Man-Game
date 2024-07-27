import random
import HangMan_art, HangMan_Words




#slecting a word and splitting into letters
chosen = random.choice(HangMan_Words.word_list)
chosen_word = [ i for i in chosen]
lives_left = 6

from HangMan_art import logo
print(logo)

display = []
for i in chosen_word:
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've arlready guessed {guess}")
    
    for postion in range(len(chosen_word)):
        letter = chosen_word[postion]
        if letter == guess:
            display[postion] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives_left -= 1
        if lives_left == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen}")
    
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")
    
    from HangMan_art import stages
    print(stages[lives_left])
