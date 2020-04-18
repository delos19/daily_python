# By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum
# of the even-valued terms.
# Project Euler Problem 2

evens = []

def fib(i, prev):
    total = 0
    while i < 4000000:
        evensCheck(i)
        temp = i
        i += prev
        prev = temp

def evensCheck(i):
    if i % 2 == 0:
        evens.append(i)
        
def sumPrint():
    total = sum(evens)
    print(evens)
    print('The sum of the evens is: \n', total)

def main():
    fib(1,1)
    sumPrint()

main()
