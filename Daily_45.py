from random import randint

def rand5_to7():
    r = 0
    for _ in range(7):
        r += randint(1, 5)
    return (r % 7) + 1


# Test the function
x = [0] * 8
for _ in xrange(20000):
    x[rand5_to7()] += 1
print  x
