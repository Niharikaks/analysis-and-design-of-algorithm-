

import matplotlib.pyplot as plt
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


n_list=[5000,6000,7000,8000,9000,10000]
sort_time=[]

for n in n_list:
    arr=[random.randint(1,100)for _ in range(n)]
    s_t= time.time()
    insertion_sort(arr)
    e_t=time.time()

    sort_time.append(e_t-s_t)
print("input sizes:",n_list)
print("sorting times",sort_time)

plt.plot(n_list,sort_time,marker='.')
plt.xlabel("Input Size (n)")
plt.ylabel("Time")
plt.title("Insertion Sort Time Complexity")
plt.grid(False)

plt.show()

