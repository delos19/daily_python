import numpy as np
x = np.array([[7, 8, 9], [2, 3, 6], [5, 6, 7]])
y = np.array([[3, 4, 5], [1, 2, 4], [5, 7, 8]])
add = np.add(x, y)  # Adds two matrices together
subtract = np.subtract(x, y)
multiply = np.multiply(x, y)
divide = np.divide(x, y)
dot = np.dot(x, y)  # This is the dot product of the two matrices
root = np.sqrt(x)  # This is the square root of this matrix
total = np.sum(x)   # Sums all the elements of a particular matrix
col_total = np.sum(y, axis=0)  # Column wise addition
row_total = np.sum(y, axis=1)  # Row wise addition
x_t = x.T  # How to transpose a matrix.
y_t = y.T

print(x, y, add, subtract, multiply, divide, dot, root, total, col_total, row_total, x_t, y_t)   # Prints out matrix

a = abs(-20)  # Calculating the absolute value
b = bin(210)  # Convert over to a binary number
print(a, b)   # Print out the statements