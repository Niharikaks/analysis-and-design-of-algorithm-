

import random

n = 6
l = [random.randint(1, 10000) for _ in range(n)]

n_len = len(l)
for i in range(n_len):
    for j in range(0, n_len - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print("Sorted list:", l)


    