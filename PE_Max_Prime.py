import math

num = 600851475143
prime =[]

if num > 1:
    for i in range(2,math.ceil(math.sqrt(num))):
        while (num % i) == 0:
            prime.append(i)
            num = num / i

print(num)
print(prime)
print('The max prime factor is: ', prime[-1])
