# Variant on the knacksack problem

def find_sequence(seq, sol, i, K):
    res_sum = sum(sol)
    if res_sum == K:
        return sol
    if res_sum > K:
        return None
    if i < 0:
        return None 
    
    for x in xrange(i, -1, -1):
        a = find_sequence(seq, sol.union([seq[i]]), i-1, K)
        if a is not None:
            return a
        b = find_sequence(seq, sol, i-1, K) 
        if b is not None:
            return b

    return None

print find_sequence([12,25,3,1,8,7], set(), 5, 21)
