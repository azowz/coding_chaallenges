from typing import List

def sum_even(arr: List[int]) -> int:
    x = 0
    for num in arr:  # Loop directly over the elements in the list
        if num % 2 == 0:  # Check if the number is even
            x += num  # Add the even number to the sum
    return x

arr = [11, 0, 5, 22]
print(sum_even(arr))  # Expected output: 22
