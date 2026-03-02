# Analysis and Comparasion Sorting Algorithms: Selection Sort vs Insertion Sort

Sorting is one of the basic topics in programming. In this article, I compare two simple sorting algorithms: Selection Sort and Insertion Sort. The goal is to understand how they work and see how fast they run in different situations.

## Short Explanation of Each Algorithm

Selection Sort works by finding the smallest value in the unsorted part of the list and moving it to the front. It repeats this step until all data is sorted. The process is simple, but it always checks the remaining data fully, even if the list is already sorted.

Insertion Sort works step by step. It takes one element and places it in the correct position among the elements that are already sorted. Because of this, it can work much faster if the data is already sorted or almost sorted.

## Time and Space Complexity

In general, both algorithms have the same average and worst-case time complexity:

$$
T(n) = O(n^2)
$$

This means the running time increases quickly as the data size becomes larger.

However, Insertion Sort has a better best-case time complexity when the data is already sorted:

$$
T(n) = O(n)
$$

Selection Sort does not change its behavior, even if the data is sorted.

For space usage, both algorithms are efficient because they only need:

$$
S(n) = O(1)
$$

This means they do not need extra memory that grows with input size.

## Testing Method

To compare performance, I used time.perf_counter() in Python to measure execution time. I tested different data sizes: 100, 500, 1000, and 2000 elements.

There were two types of data:

- Random data

- Already sorted data

Each algorithm was tested using the same datasets to make the comparison fair.

## Results and Discussion

For random data, both algorithms showed similar behavior. The running time increased a lot when the input size increased. Insertion Sort was usually a bit faster because it stops moving elements once the correct position is found. Selection Sort always scans the remaining list completely.

For sorted data, the difference was clear. Insertion Sort became much faster because it only needed small checks and almost no shifting. Its performance was close to linear time. Selection Sort, on the other hand, still checked all remaining elements every time, so its speed did not improve much.

## Practical Use

Insertion Sort is a good choice for:

- Small datasets

- Nearly sorted data

Selection Sort is mostly useful for learning purposes because it is easy to understand.

For large datasets, both algorithms are not recommended. Faster algorithms with O(n log n) complexity are better for real applications.

## Conclusion

Both Selection Sort and Insertion Sort are simple and important to learn. They help us understand how sorting works and how time complexity affects performance.

Even though they are not used often in real systems, learning these basic algorithms builds a strong foundation before moving to more advanced sorting methods.

