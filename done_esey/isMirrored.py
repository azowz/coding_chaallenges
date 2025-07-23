def isMirrored(num: int) -> bool:
    num_str = str(num)  # Convert the number to a string
    num_reversed = num_str[::-1]  # Reverse the string

    return num_str == num_reversed  # Check if the original and reversed strings are the same


print(isMirrored(11))