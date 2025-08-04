from typing import List
def delete_element_in_array(arr: List[int], index: int) -> List[int]:
    i = 0
    while i < len(arr):
        if arr[i] == index:
            arr.pop(i)
        else:
            i += 1
    return arr

# اختبار الدالة
arr = [3, -3, 4, 0]
index = 0
result = delete_element_in_array(arr, index)
print(result)  # يجب أن تطبع [1, 2, 4, 5]
