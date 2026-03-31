import time
import numpy as np
import matplotlib.pyplot as plt
import sys
import random
import argparse

sys.setrecursionlimit(10000)


def insertion_sort(arr):
    arr_copy = list(arr)
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # החלפת איברים
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

################################-part B-########################################
sizes = [100, 500, 1000, 3000, 5000]
iterations = 5
algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}

results = {name: {"avg": [], "std": []} for name in algorithms}

for size in sizes:
    for name, func in algorithms.items():
        run_times = []
        for _ in range(iterations):
            test_arr = np.random.randint(0, 1000000, size=size).tolist()
            start = time.perf_counter()
            func(test_arr)
            end = time.perf_counter()
            run_times.append(end - start)
        results[name]["avg"].append(np.mean(run_times))
        results[name]["std"].append(np.std(run_times))

plt.figure(figsize=(10, 6))
for name in algorithms:
    plt.errorbar(sizes, results[name]["avg"], yerr=results[name]["std"],
                 label=name, marker='o', capsize=5)

plt.title('Part B: Comparison of Sorting Algorithms Running Time')
plt.xlabel('Array Size (n)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('result1.png')
plt.show()

################################-part C-########################################

def generate_nearly_sorted(size, noise_percent):
    arr = list(range(size))
    num_swaps = int(size * noise_percent)
    for _ in range(num_swaps):
        idx1 = random.randint(0, size - 1)
        idx2 = random.randint(0, size - 1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

sizes = [100, 500, 1000, 2000, 3000]
noise_levels = [0.05, 0.20]
iterations = 5
algorithms = {
    "Selection Sort": selection_sort,
    "Quick Sort": quick_sort,
    "Insertion Sort": insertion_sort
}

for noise in noise_levels:
    results_noise = {name: [] for name in algorithms}
    print(f"\nStarting Part C with Noise Level: {int(noise * 100)}%")

    for size in sizes:
        for name, func in algorithms.items():
            run_times = []
            for _ in range(iterations):
                test_arr = generate_nearly_sorted(size, noise)
                start = time.perf_counter()
                func(test_arr)
                end = time.perf_counter()
                run_times.append(end - start)
            results_noise[name].append(np.mean(run_times))
        print(f"Finished size {size} for {int(noise * 100)}% noise")

    plt.figure(figsize=(10, 6))
    colors = ['#ff7f0e', '#2ca02c', '#1f77b4']

    for i, (name, times) in enumerate(results_noise.items()):
        plt.plot(sizes, times, label=name, marker='o', color=colors[i], linewidth=2)

    plt.title(f'Part C: Nearly Sorted Comparison (Noise={int(noise * 100)}%)')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Runtime (seconds)')
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper right')
    plt.tight_layout()

    filename = f'result2_{int(noise * 100)}percent.png'
    plt.savefig(filename)
    print(f"Plot saved as {filename}")
    plt.show()

################################-part D-########################################

ALGO_MAP = {
    1: ("Bubble Sort", bubble_sort),
    2: ("Selection Sort", selection_sort),
    3: ("Insertion Sort", insertion_sort),
    4: ("Merge Sort", merge_sort),
    5: ("Quick Sort", quick_sort)
}


def generate_array(size, exp_type):
    if exp_type == 0:  # Random (Part B)
        return np.random.randint(0, 1000000, size=size).tolist()
    elif exp_type == 1:  # 5% Noise (Part C)
        arr = list(range(size))
        for _ in range(int(size * 0.05)):
            i, j = random.randint(0, size - 1), random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    elif exp_type == 2:  # 20% Noise (Part C)
        arr = list(range(size))
        for _ in range(int(size * 0.20)):
            i, j = random.randint(0, size - 1), random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr


def main():
    parser = argparse.ArgumentParser(description="Sorting Algorithms Experiment Runner")
    parser.add_argument("-a", "--algos", nargs="+", type=int, required=True, help="IDs of algorithms (1-5)")
    parser.add_argument("-s", "--sizes", nargs="+", type=int, required=True, help="Array sizes")
    parser.add_argument("-e", "--experiment", type=int, default=0, help="0:Random, 1:5% Noise, 2:20% Noise")
    parser.add_argument("-r", "--reps", type=int, default=5, help="Number of repetitions")

    args = parser.parse_args()

    results = {algo_id: {"avg": [], "std": []} for algo_id in args.algos}

    for size in args.sizes:
        for algo_id in args.algos:
            name, func = ALGO_MAP[algo_id]
            times = []
            for _ in range(args.reps):
                arr = generate_array(size, args.experiment)
                start = time.perf_counter()
                func(arr)
                times.append(time.perf_counter() - start)
            results[algo_id]["avg"].append(np.mean(times))
            results[algo_id]["std"].append(np.std(times))

    plt.figure(figsize=(10, 6))
    for algo_id in args.algos:
        name = ALGO_MAP[algo_id][0]
        plt.plot(args.sizes, results[algo_id]["avg"], label=name, marker='o')

    plt.title(f"Experiment Type {args.experiment} Results")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True, alpha=0.3)

    filename = "result1.png" if args.experiment == 0 else "result2.png"
    plt.savefig(filename)
    print(f"Results saved to {filename}")
    plt.show()

if __name__ == "__main__":
    main()