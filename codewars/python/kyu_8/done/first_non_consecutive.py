def first_non_consecutive(arr):
    consecutive = arr[1] - arr[0] if len(arr) > 1 else 1  # default diff = 1
    print("Consecutive difference:", consecutive)
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != consecutive:
            if arr[i] - arr[i - 1] :
                print("Found non-consecutive element:", arr[i])
            return arr[i-1] 
    return None


def first_non_consecutive(arr):
    if len(arr) < 2:
        return None
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None

print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))  # Should return 6

print(first_non_consecutive([1, 2, 3, 4, 5]))  # Should return None
print(first_non_consecutive([4,6,7,8,9,11]))  # Should return None