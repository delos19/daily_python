a = 999
b = 999
pal = []

def iterateProduct(a, b):
    for i in range(a, 100, -1):
        for j in range(b, 100, -1):
            product = i * j
            if isPalendrome(product) is True:
                break
            else:
                isPalendrome(product)
                


def isPalendrome(product):
    product = str(product)
    rev_prod = reversed(product)
    if list(product) == list(rev_prod):
        pal.append(int(product))
        return True
    else:
        return False

iterateProduct(a, b)
print(pal)
print('The largest pallendrome is: ', max(pal))
