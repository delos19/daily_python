a = 999
b = 999
pal = []

# This function iterates the product of a and b
# It also appends all pallendromes to the list pal
def iterateProduct(a, b):
    for i in range(a, 100, -1):
        for j in range(b, 100, -1):
            product = i * j
            isPalendrome(product) # sends product to be evaluated
                
# This function determines if the product is a pallendrome
# Using the product and the reversed() function to
# determine string equivalence
def isPalendrome(product):
    product = str(product)
    rev_prod = reversed(product)
    if list(product) == list(rev_prod):
        pal.append(int(product))

# Main function for program
def main(alpha, bravo):
    iterateProduct(alpha, bravo)
    print('The largest pallendrome is: ', max(pal))

main(a, b)
