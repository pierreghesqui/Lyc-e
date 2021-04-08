import random

colors = ['red', 'blue', 'green', 'pink', 'yellow', 'orange', 'black', 'purple', 'brown']

randomNumber = random.randint(0, 8)
answer = 'I am ' + colors[randomNumber]

for i in range(0, 3):
    response = input(f'What color am I thinking of ? {colors}')
    if response == colors[randomNumber]:
        print("Correct ! You guessed it right")
        break

    else:
        if i == 2:
            print("Wrong ! You ran out of guesses")
        else:
            print("Wrong  Try again")

print(answer)
