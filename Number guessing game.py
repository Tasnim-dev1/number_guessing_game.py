import random
print('**Number Guessing Game**')
print('Guess a number between 1 and 10')
answer = random.randrange(1,10)

while True:
    Guessing = int(input("answer : "))
    if Guessing > answer:
        print("too high")
    elif Guessing < answer:
        print("too low")
    else:
        print("bingooooo!!you win")
        break
