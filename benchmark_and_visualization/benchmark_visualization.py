import random
import time
import matplotlib.pyplot as plt

# ==============================
# Sorting Algorithms
# ==============================

def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ==============================
# Benchmark Function
# ==============================

def benchmark(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return end - start


# ==============================
# Run Benchmark
# ==============================

sizes = [100, 500, 1000, 2000]

selection_random = []
insertion_random = []

selection_sorted = []
insertion_sorted = []

for size in sizes:
    
    # Random data
    data_random = [random.randint(0, 10000) for _ in range(size)]
    
    selection_random.append(benchmark(selection_sort, data_random))
    insertion_random.append(benchmark(insertion_sort, data_random))
    
    # Already sorted data
    data_sorted = sorted(data_random)
    
    selection_sorted.append(benchmark(selection_sort, data_sorted))
    insertion_sorted.append(benchmark(insertion_sort, data_sorted))


# ==============================
# Visualization
# ==============================

plt.figure()
plt.plot(sizes, selection_random)
plt.plot(sizes, insertion_random)
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Random Data Performance")
plt.legend(["Selection Sort", "Insertion Sort"])
plt.show()

plt.figure()
plt.plot(sizes, selection_sorted)
plt.plot(sizes, insertion_sorted)
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Sorted Data Performance")
plt.legend(["Selection Sort", "Insertion Sort"])
plt.show()
