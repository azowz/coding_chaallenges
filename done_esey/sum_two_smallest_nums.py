from typing import List

def sum_two_smallest_nums(arr: List[int]) -> int:
    # Sort the list in ascending order
    arr.sort()
    
    # Return the sum of the two smallest numbers
    return arr[0] + arr[1]


arr = [2, 5, 6, 7, 3]
ar =arr.sort()
print (ar)
print(sum_two_smallest_nums(arr))  # Output: 5