import time
import random


def quick_sort(arr):
    """快速排序"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 取中間當基準
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """合併排序"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # 遞回左半邊
    right = merge_sort(arr[mid:])  # 遞回右半邊
    return merge(left, right)


def merge(left, right):
    """合併排序"""
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


def test_sorting_methods(nums):
    print("Original array:", nums)

    # 快速排序
    start_time = time.perf_counter()
    quick_sorted = quick_sort(nums.copy())
    quick_time = time.perf_counter() - start_time
    print(f"Quick Sort time: {quick_time:.6f} seconds")
    print("Quick Sorted array:", quick_sorted)

    # 合併排序
    start_time = time.perf_counter()
    merge_sorted = merge_sort(nums.copy())
    merge_time = time.perf_counter() - start_time
    print(f"Merge Sort time: {merge_time:.6f} seconds")
    print("Merge Sorted array:", merge_sorted)


# 示例
nums = [3747, 4195, 1321, 7881, 1954, 3406, 90, 7456, 6807, 3527, 3478, 3123, 5850, 1002, 73, 416, 9239, 48, 5619, 3728, 9754, 8156, 2301, 216, 8412, 94, 13, 59, 5839, 5427]
test_sorting_methods(nums)
