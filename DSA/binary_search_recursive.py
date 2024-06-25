from typing import List


def binary_search_recursive(array: List[int], x: int, low: int, high: int):
    if high >= low:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search_recursive(array=array, x=x, low=low, high=mid - 1)
        else:
            return binary_search_recursive(array=array, x=x, low=mid + 1, high=high)
    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]

x = 4

result = binary_search_recursive(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
