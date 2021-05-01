import random 
value=random.randint(1,9)
print(value)
for i in range(1,5):
    guess=int(input("Guess a number between 1 to 9:"))
    if guess==value:
        print("Your guess was correct")
        break
    elif guess<value:
        print("Your guess was too low")
    elif guess>value:
        print("Your guess was too high")
        