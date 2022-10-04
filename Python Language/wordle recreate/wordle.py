import random

rlrp = "🟩"
rlwp = "🟨"
wl = "⬛"
history = ["history"]
with open('words.txt', 'r') as f:
    words = [w.strip() for w in f.readlines()]

for i in range(10):
    print("\nStarting a game...\n")
    current_word = random.choice(words)
    if history[-1] != current_word:
        history.append(current_word)
        guesses = 6
        while guesses>0:
            guess = input(f"Guess/es left {guesses}: ")
            print(f"\nYou guessed: {guess.upper()}")
            if guess == "x" or len(guess)==0:
                print("ty for playing!\n")
                break
            elif words.count(guess.lower())<1:
                print("Your guess is not in the word list.\n")
                continue
            elif len(guess)!=5:
                print("Please use 5 lettered words only!\n")
                continue
            else:
                check_guess = []
                for i in range(len(guess)):
                    if guess[i]==current_word[i]:
                        check_guess.append(rlrp)
                    elif current_word.count(guess[i])>0:
                        check_guess.append(rlwp)
                    else:
                        check_guess.append(wl)
                
                if check_guess.count(rlrp)==5:
                    print(f"{''.join(check_guess)}\nYOU WIN!\n")
                    break
                
                print(f"Hints: {''.join(check_guess)}\n\nGuess Again!")
                guesses -= 1
                if guess==0:
                    print("No guesses left!\n")
                    break
        print(f"the Word is: {current_word.upper()}\n")