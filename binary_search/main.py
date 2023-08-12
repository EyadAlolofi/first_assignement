"""
In the code, we define the binary_search function that takes an array (arr) and a target element (target) as parameters and returns the index of the target element if found, or -1 if not found. The function uses the binary search algorithm to perform the search.
"""
def binary_search(arr, target):
    start = 0
    # end = len(arr) - 1
    end = len(arr)

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


arr = [2, 4, 6, 8, 10, 12, 14]

target = input("Enter a number: ")

result = binary_search(arr, int(target))

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")
