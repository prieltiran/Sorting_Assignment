# Sorting Algorithms Comparison Project
#Data Structures and Algorithms
## Student Details
* **Student Name:** [Priel Tiran]
* **Student Name:** [Omer Dagan]

## Selected Algorithms
In this assignment, we compared the following algorithms:
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort

---

## Part B - Comparative Experiment (Random Arrays)
Below is the performance comparison of the algorithms on arrays filled with random integers.

![Result 1](result1.png)

**Short Explanation:**
In this graph, we can see that as the array size increases, the execution time for **Bubble Sort**, **Selection Sort**, and **Insertion Sort** grows quadratically ($O(n^2)$). In contrast, **Quick Sort** and **Merge Sort** ($O(n \log n)$) remain extremely fast and efficient even for larger datasets.

---

## Part C - Nearly Sorted Arrays (Noise Analysis)
In this experiment, we started with a sorted array and added random "noise" (5% or 20% random swaps).

![Result 2](result2.png)

**Analysis of Results:**
* **How the running times changed:** The most notable change is seen in **Insertion Sort**, which performed significantly faster than it did in the random experiment. **Quick Sort** and **Merge Sort** remained very efficient, while **Selection Sort** showed almost no change in performance.
* **Why this happened:** * **Insertion Sort** is an "adaptive" algorithm. When the array is nearly sorted, it performs fewer operations because the elements are already close to their final positions. 
    * **Selection Sort** is not adaptive; it always scans the entire remaining array to find the minimum value, regardless of its initial order, which is why its time remained constant ($O(n^2)$).
