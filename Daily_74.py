# Function with a cuadratic cost, just iterate trough
# each position of the matrix and check it is the element
# we are looking for.
def f1(n, X):
    total = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if x * y == X:
                total += 1

    return total


# Function with a linear cost, the number we are looking X
# must be formed by the multiplication of two others (X = a * b)
# In this solution we iterate trough each number from 1 to n to
# check if the number can either be a or b (X % x == 0)
# Then we only have to check if the other number is less than n
# to update the solution counter (X / x give us the other number).
def f2(n, X):
    total = 0

    for x in range(1, n + 1):
        if (X % x) == 0:
            if (X / x) <= n:
                total += 1

    return total


print(f1(6, 12))
print(f2(6, 12))
