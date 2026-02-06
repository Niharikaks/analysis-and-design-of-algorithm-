import matplotlib.pyplot as plt
import random
import time


def merge_sort(a):
    n = len(a)
    if n > 1:
        b = a[:n//2]
        c = a[n//2:]
        print(b, "|", c)
        merge_sort(b)
        merge_sort(c)
        merge(a, b, c)

def merge(a, b, c):
    n1 = len(b)
    n2 = len(c)
    i = j = k = 0

    while i < n1 and j < n2:
        if b[i] < c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1

    while i < n1:
        a[k] = b[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = c[j]
        j += 1
        k += 1

    print(a)

a = [6, 5, 1, 3, 4, 2]
merge_sort(a)
print("Sorted array:", a)

n_list=[5000,6000,7000,8000,9000,10000]
sort_time=[]

for n in n_list:
    arr=[random.randint(1,100)for _ in range(n)]
    s_t= time.time()
    merge_sort(arr)
    e_t=time.time()

    sort_time.append(e_t-s_t)
print("input sizes:",n_list)
print("sorting times",sort_time)

plt.plot(n_list,sort_time,marker='.')
plt.xlabel("Input Size (n)")
plt.ylabel("Time")
plt.title("merge Sort Time Complexity")
plt.grid(False)
plt.show()

