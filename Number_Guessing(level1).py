import random
def get_number(b):
    while True:
        try:
            a = int(input(f"Guess {b}: "))
            return a
        except ValueError:
            print("Invalid Input")
goal = random.randint(0,100)
print(goal)
i=0
guessed = False
while i<10:
    i+=1
    user_nbr = get_number(i)
    if user_nbr < goal:
        print("Too Low")
        continue
    elif user_nbr > goal:
        print("Too High")
        continue
    else:
        guessed = True
        break
    guessed = False

if guessed == True:
    print("You guessed",goal,"Right")
else:
    print("You Couldn't guess right")
    print("Number was ",goal)