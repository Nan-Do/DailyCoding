# To solve the problem use a temporal buffer, if what we want to read is bigger than what is
# left on the buffer make enough calls to read7 to fill it.
# This implementation is not reentrant, every time the function is called it reads from the
# stream from the beggining
def read7(seq, i):
    return seq[i:i + 7], i + 7


def readN(n, seq):
    i = 0
    buf = ""
    while len(buf) < n:
        temp, i = read7(seq, i)
        buf += temp

    ret = buf[:n]
    buf = buf[n:]

    return ret


s = "Hello world this is wonderful!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
q = readN(22, s)
print(q, len(q))
