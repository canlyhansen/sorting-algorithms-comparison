## Sorting Algorithm Performance Comparison — Explanation

Description:
This project analyzes and compares the performance of two sorting algorithms. They are Insertion Sort and Selection Sort.
The goal is not only to implement these algorithms, but also to evaluate how efficient they are in terms of execution time and scalability when handling different types of data.

Objectives:
1. Understand how each sorting algorithm works internally.
2. Compare their theoretical time and space complexity.
3. Measure their empirical performance using real runtime experiments.

Methodology:
Dataset Types:
The algorithms are tested on three types of input data:
- Random data: Unsorted random integers
- Sorted data: Already sorted list
This is important because some algorithms perform differently depending on input order.

Data Sizes:
The experiments use multiple input sizes to observe scalability:
- 100 elements
- 500 elements
- 2000 elements
- 10000 elements

This helps analyze how performance grows as the dataset becomes larger.

Time Measurement:
Execution time is measured using time.perf_counter() to obtain precise runtime values.
This allows objective comparison instead of relying only on theoretical complexity.

Expected Results / Insights:
1. Both algorithms have O(n^2) complexity, so they become very slow when the input size increases significantly.
2. Input order (random and sorted) can strongly affect runtime, showing that algorithm performance depends on data characteristics.

Big Picture Summary:
This project follows a complete analytical workflow:
1. Implement sorting algorithms
2. Generate datasets of different types and sizes
3. Benchmark execution time
4. Visualize results using plots
5. Interpret insights based on empirical evidence

This makes the project valuable for demonstrating both programming skills and data analysis thinking in performance evaluation.
