from algorithms.insertion import insertion
from algorithms.selection import selection

from benchmark_and_visualization import benchmark_visualization

algorithms = {
    "Insertion": insertion,
    "Selection": selection,
}

sizes = [100, 1000, 3000]
cases = ["random", "sorted", "reversed"]

results = run_benchmark(algorithms, sizes, cases)

for case in cases:
    plot_results(results, sizes, case)
