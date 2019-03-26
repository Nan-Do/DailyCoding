def find_rotated(s, k):
    lo = 0
    hi = len(s) - 1

    while lo <= hi:
        mid = int((lo + hi) / 2)

        if s[mid] == k:
            return mid

        if s[lo] <= s[mid]:
            if s[lo] <= k < s[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if s[mid] < k <= s[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return -1


s = [13, 18, 25, 2, 8, 10]

print(find_rotated(s, 8))
print(find_rotated(s, 10))
print(find_rotated(s, 11))
print(find_rotated(s, 13))
print(find_rotated(s, 12))
