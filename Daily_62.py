def compute_paths():
    cache = {}

    def _compute_paths(n, m):
        if (n, m) in cache:
            return cache[(n, m)]

        if n == 1 or m == 1:
            cache[(n, m)] = 1
        else:
            cache[(n, m)] = _compute_paths(n - 1, m) + _compute_paths(n, m - 1)

        return cache[(n, m)]

    return _compute_paths


compute_paths = compute_paths()

print(compute_paths(2, 2))
print(compute_paths(3, 3))
print(compute_paths(5, 5))
