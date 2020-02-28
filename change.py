price = input("How much is the item? \n")
cash_offered = input("How much cash do you have? \n")

dollar = 1
quarter = 0.25
dime = 0.1
nickel = 0.05
penny = 0.01

if cash_offered < price:
    print("You cannot afford this item")
else:
    q = cash_offered % quarter
    qrm = cash_offered - (q * quarter)
    d = qrm % dime
    drm = qrm - (d * dime)
    n = drm % nickel
    nrm = drm - (n * nickel)
    p = nrm % penny
    print("You should get %s quarters, %s dimes, %s nickels, %s pennies" % (q, d, n, p))
