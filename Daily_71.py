import random

# General way to solve it:
# The generator number we have is greater than the one we are requested
# just keep generating numbers until the generated number is on the 
# requested range
def from_rand7_to_rand5():
    v = -1

    while v < 0 or v >= 5:
        v = int(random.random() * 7)

    return v + 1


values = [0] * 6
for _ in range(100000):
    values[from_rand7_to_rand5()] += 1

print(values)
