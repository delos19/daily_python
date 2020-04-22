
a = 999
b = 999

def iterateProduct(a, b):
    for i in range(999, 100):
        for j in range(999, 100):
            product = i * j
            j += -1
            if isPalendrome(product) is True:
                print('The largest pallendrome is: ', product)
            else:
                isPalendrome(product)
                print('Did not work, continuing...')
        i += -1
    

def isPalendrome(product):
    product = str(product)
    rev_prod = reversed(product)
    if list(product) == list(rev_prod):
        print('Should be good')
    else:
        print('Did not work, continuing...')

print(a,b)
iterateProduct(a, b)
print(a,b)
