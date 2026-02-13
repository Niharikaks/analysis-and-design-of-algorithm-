import matplotlib.pyplot as plt
import random
import time 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]  
        left = []
        right = []

        for i in range(len(arr) - 1):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])

        return quick_sort(left) + [pivot] + quick_sort(right)
    

n_list=[5000,6000,7000,8000,9000,10000]
sort_time=[]

for n in n_list:
    arr=[random.randint(1,100)for _ in range(n)]
    s_t= time.time()
    quick_sort(arr)
    e_t=time.time()

    sort_time.append(e_t-s_t)
print("input sizes:",n_list)
print("sorting times",sort_time)

plt.plot(n_list,sort_time,marker='.')
plt.xlabel("Input Size (n)")
plt.ylabel("Time")
plt.title("quick sort Time Complexity")
plt.grid(True)

plt.show()

    

