primes = [11, 13, 14, 16, 17, 18, 19, 20]
primes2 = []

def iterate(start):
    for i in range(start, 999999999, start):
        if all(i % j == 0 for j in primes):
            return i
    return None

def calcList():
    j = 2
    for i in range(2,21):
        for j in range(1, 21):
            power = i ** j
            if power < 20:
                if power not in primes2:
                    primes2.append(power)
            
            
LCF = iterate(20)
calcList()
print(LCF)
print(primes2)
