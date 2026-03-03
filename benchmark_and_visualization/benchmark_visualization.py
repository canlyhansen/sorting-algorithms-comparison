import random
import time
import matplotlib.pyplot as plt

from algorithms.insertion import insertion_sort
from algorithms.selection import selection_sort

# ==============================
# Run Benchmark
# ==============================

def generate_data(size, case="random"):
    if case == "random":
        return [random.randint(0, 10000) for _ in range(size)]
    elif case == "sorted":
        return list(range(size))

def measure_time(sort_func, data):
    start = time.perf_counter()
    sort_func(data)
    end = time.perf_counter()
    return end - start

def run_benchmark(algorithms, sizes, cases):
    results = {}

    for name, func in algorithms.items():
        results[name] = {}
        for case in cases:
            results[name][case] = []
            for size in sizes:
                data = generate_data(size, case)
                exec_time = measure_time(func, data)
                results[name][case].append(exec_time)

    return results

# ==============================
# Visualization
# ==============================

def plot_results(results, sizes, case):
    for algo, data in results.items():
        plt.plot(sizes, data[case], label=algo)

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Sorting Performance ({case} data)")
    plt.legend()
    plt.show()
