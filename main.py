from algorithms.insertion import insertion_sort
from algorithms.selection import selection_sort

from benchmark_and_visualization import run_benchmark
from benchmark_and_visualization import plot_results

algorithms = {
    "Insertion": insertion_sort,
    "Selection": selection_sort,
}

sizes = [100, 500, 2000, 10000]
cases = ["random", "sorted"]

results = run_benchmark(algorithms, sizes, cases)

for case in cases:
    plot_results(results, sizes, case)
