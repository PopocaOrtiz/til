# how to
[0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
# answer
[2 * (n + sum([m for m in range(n)])) for n in range(10)]
