import random

def main():
    rangeChoice = int(input("What is the highest value for guess? \n"))
    options = list(range(1,int(rangeChoice)))
    selection = random.choice(options)
    check(selection)

def check(select):
    guess = input("Input your guess: \n")
    if int(guess) == select:
        print("You got it! The number was ", select )
    elif int(guess) < select:
        print("Too low! Try again! \n")
        check(select)
    elif int(guess) > select:
        print("Too high! Try again! \n")
        check(select)
        
main()
        
        
