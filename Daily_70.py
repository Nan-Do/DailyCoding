from itertools import count


def to_digits(n):
    res = []

    while n > 0:
        res.append(n % 10)
        n = int(n / 10)

    return res


def n_th_perfect(n, val=10):
    nums = count(1)

    while True:
        num = next(nums)
        x = to_digits(num)
        if sum(x) == val:
            n -= 1
            if n == 0:
                return num


print(n_th_perfect(1))
print(n_th_perfect(2))
