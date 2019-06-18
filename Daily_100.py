# How to compute the distance between two points?
# The distance is computed using the difference between
# the x component and the y component of each point. As
# we can traverse in diagonal too the distance is the
# maximum between these two values.
# It is a variation of the Manhattan distances.
def compute_distance(a, b):
    x_1, y_1 = a
    x_2, y_2 = b

    return max(abs(x_2 - x_1), abs(y_2 - y_1))


# Cost O(n)
# Traverse the sequence of points in pairs computing the distance
# between two points, the solution is the sum of all the distances
def minimum_movement(s):
    total_dis = 0

    for x in range(len(s) - 1):
        total_dis += compute_distance(s[x], s[x + 1])

    return total_dis


print(minimum_movement([(0, 0), (1, 1), (1, 2)]))
