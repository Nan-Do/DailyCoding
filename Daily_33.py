import heapq

def f(s): 
    min_h = [s[0]]
    max_h = []

    for x in xrange(1, len(s)):
        v = s[x]

        if len(min_h) == len(max_h):
            print (min_h[0] - max_h[0]) / 2.0
        elif len(max_h) > len(min_h):
            print -max_h[0]
        else:
            print min_h[0]

        if v < min_h[0]:
            heapq.heappush(max_h, -v)
        else:
            heapq.heappush(min_h, v)


        while len(min_h) - len(max_h) >= 2:
            heapq.heappush(max_h, -heapq.heappop(min_h))
        while len(max_h) - len(min_h) >= 2:
            heapq.heappush(min_h, -heapq.heappop(max_h))

f([2,1,5,7,2,0,5])
