num = 46337
newNum = num
largestFactor = 0
counter = 2

while counter * counter <= newNum:
    if (newNum % counter == 0):
        newNum = newNum / counter
        largestFactor = counter
    else:
        counter += 1
if newNum > largestFactor:
    largestFactor = newNum

print(largestFactor)
