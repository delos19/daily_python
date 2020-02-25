def quick(gallons, cost):
    total = int(gallons) * int(cost)
    print("The total cost of gas is: $" + str(total))


def test_Function(first, last):
    print("Your name is: " + first + " " + last)

first = input("What is your first name? \n")
last = input("What is your last name? \n")

gallons = input("How many gallons is your tank \n")
cost = input("How much is gas currently \n ")


test_Function(first, last)
quick(gallons, cost)
