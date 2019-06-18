from time import localtime, sleep


# The problem can be solved with a clousure that wraps the calling to the sleep function before
# calling the function
def debounced(f, N):
    def _f():
        sleep(N)
        f()

    return _f


def sum():
    return 2 + 2


s = debounced(sum, 2)

print(localtime())
s()
print(localtime())
