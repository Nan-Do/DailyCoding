def merge(arr, lo, mid, hi):
    temp = [0] * (hi - lo + 1)

    inversions = 0
    current = 0
    s1 = lo
    s2 = mid+1

    while s1 <= mid and s2 <= hi:
        if arr[s1] <= arr[s2]:
            temp[current] = arr[s1]
            s1 += 1
        else:
            temp[current] = arr[s2]
            s2 += 1
            inversions += mid+1 - s1
        current += 1

    s = s2
    if s1 <= mid:
        s = s1
        
    for x in xrange(current, len(temp)):
        temp[x] = arr[s]
        s += 1

    current = lo
    for x in temp:
        arr[current] = x
        current += 1

    return inversions




def merge_sort_inversions(arr, lo, hi):
    inversions = 0
    if lo < hi:
        mid = (lo + hi) / 2
        inversions += merge_sort_inversions(arr, lo, mid)
        inversions += merge_sort_inversions(arr, mid+1, hi)
        inversions += merge(arr, lo, mid, hi)

    return inversions


a = [5,4,3,2,1]
print merge_sort_inversions(a, 0, 4)
a = [2,4,1,3,5]
print merge_sort_inversions(a, 0, 4)
print a
