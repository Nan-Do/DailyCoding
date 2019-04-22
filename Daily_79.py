# Cost O(n)
# I got tricked by the condition that nums[i] < nums[i + 1].
# Better test cases would have helped to detect this error. For example, [9, 10, 7, 11, 13].
# Here if you change the number 10 you also have to change number 7 later but it can be done
# with just one change, that is, changing just number 7
# The real invariant is: nums[i - 1] < nums[i] < nums[i + 1], so all 3 numbers need to meet the condition.
# If the relationthips between nums[i - 1] && nums[i + 1] is wrong, fix them by chaning one of the 3 numbers:
# 1. nums[i] > nums[i + 1] && nums[i - 1] > nums[i + 1]:
#     because numbers ahead if i - 1 is correct, so lower the later, nums[i + 1] = nums[i]
# 2. nums[i] > nums[i + 1] && nums[i - 1] < nums[i + 1]:
#     raise nums[i] since it's already greater than nums[i - 1], nums[i] = nums[i + 1]
#     I think this condition would be better to change it to num[i] = num[i - 1]
#     As it is easier to keep the invariants when you change the numbers with the lower possible values
# 3. if i == 0 && nums[i] > nums[i + 1], there is no i-1 to worry about, directly count++;
def can_transform_array(seq):
    increasing_reversed = 0

    for x in range(len(seq) - 1):
        if seq[x] > seq[x + 1]:
            if x > 0 and seq[x - 1] > seq[x] + 1:
                seq[x + 1] = seq[x]
            if x > 0 and seq[x - 1] < seq[x] + 1:
                seq[x] = seq[x - 1]
            increasing_reversed += 1

    return (increasing_reversed <= 1)


print(can_transform_array([10, 5, 7]))
print(can_transform_array([10, 5, 1]))
