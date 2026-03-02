# 📊 Performance Analysis: Selection Sort vs Insertion Sort
## 📌 Project Overview

This project analyzes and compares the performance of two fundamental sorting algorithms:

- Selection Sort

- Insertion Sort

The objective of this analysis is to:

- Understand how each algorithm works

- Compare their theoretical time and space complexity

- Measure empirical performance using Python benchmarking

- Analyze performance differences on random and sorted data

## 🔎 1. Algorithm Overview

### 1.1 Selection Sort

Selection Sort works by repeatedly selecting the smallest element from the unsorted portion and placing it at the beginning.

Key Characteristics:

- Always performs the same number of comparisons

- Not adaptive (performance does not improve if data is sorted)

- Simple implementation

### 1.2 Insertion Sort

Insertion Sort builds the sorted array gradually by inserting each new element into its correct position within the already sorted portion.

Key Characteristics:

- Adaptive (performance improves if data is nearly sorted)

- Efficient for small datasets

- Used in hybrid sorting algorithms

## 📐 2. Theoretical Time Complexity

Both algorithms have quadratic growth in average and worst-case scenarios.

| Case             | Selection Sort | Insertion Sort |
| ---------------- | -------------- | -------------- |
| Best Case        | O(n²)          | O(n)           |
| Average Case     | O(n²)          | O(n²)          |
| Worst Case       | O(n²)          | O(n²)          |
| Space Complexity | O(1)           | O(1)           |


**Important Insight**

- Selection Sort always performs ~n² comparisons.

- Insertion Sort adapts to input structure.

- On already sorted data, Insertion Sort runs in linear time:

## 🧪 3. Benchmark Methodology

Benchmarking was performed using:

- time.perf_counter() for execution timing

- Multiple input sizes: 100, 500, 1000, 2000

- Two data conditions:
    - Random data
    - Already sorted data

Each algorithm was tested independently using identical datasets.

## 📊 4. Benchmark Results

### 4.1 Random Data

Observations:

- Both algorithms show quadratic growth.

- Execution time increases significantly as input size increases.

- Insertion Sort is generally slightly faster than Selection Sort.

**Why?**

Selection Sort always scans the entire unsorted portion.

Insertion Sort stops shifting elements once the correct position is found.

### 4.2 Sorted Data

This is where the difference becomes significant.

Observations:

- Selection Sort performance remains O(n²).

- Insertion Sort performance improves dramatically.

- Insertion Sort approaches linear time complexity.

**Explanation**

Insertion Sort only performs minimal comparisons when the array is already ordered.

Selection Sort still performs full scans regardless of input condition.

## 📈 5. Performance Interpretation

Algorithm Adaptability

Selection Sort:

- Non-adaptive

- Predictable but inefficient

Insertion Sort:

- Adaptive

- Highly sensitive to input order

**Practical Implications**

| Scenario            | Recommended Algorithm               |
| ------------------- | ----------------------------------- |
| Small dataset       | Insertion Sort                      |
| Nearly sorted data  | Insertion Sort                      |
| Educational purpose | Both                                |
| Large dataset       | Neither (use O(n log n) algorithms) |


## ⚠️ Limitations

- Quadratic complexity makes both algorithms unsuitable for large-scale systems.

- Benchmark results may vary depending on hardware.

- Not compared against modern algorithms (Merge Sort, Quick Sort, Timsort).

## 🏁 6. Conclusion

This analysis demonstrates that:

1. Both algorithms have O(n²) average complexity.

2. Insertion Sort is adaptive, while Selection Sort is not.

3. Insertion Sort significantly outperforms Selection Sort on nearly sorted data.

4. Neither algorithm is suitable for large datasets compared to O(n log n) algorithms.

Although rarely used in production systems, both algorithms are essential for understanding:

- Fundamental sorting mechanics

- Algorithm complexity growth

- The impact of input structure on performance

Mastering these basic algorithms provides a strong foundation for understanding more advanced sorting techniques.