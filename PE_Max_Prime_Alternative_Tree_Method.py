# This method uses a different iteration
# approach to solving the maximum prime
# number calculator

num = 46337
newNum = num
largestFactor = 0
counter = 2

while counter * counter <= newNum: # denotes the square counter comparison
    if (newNum % counter == 0): # verifies if it is not prime
        newNum = newNum / counter
        largestFactor = counter
    else: # it is a prime factor
        counter += 1
if newNum > largestFactor:
    largestFactor = newNum

print(largestFactor)
