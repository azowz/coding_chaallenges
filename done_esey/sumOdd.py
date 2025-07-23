from typing import List

def sumOdd(arr: List[int]) -> int:
    x = 0
    for i in range(len(arr)):  # Use range(len(arr)) to iterate over indices
        if arr[i] % 2 == 1:  # Check if the element at index i is odd
            x += arr[i]  # Add the odd number to the sum
    return x 

arr = [2, 9, 5, 4, 0]
print(sumOdd(arr))  # Expected output: 14
