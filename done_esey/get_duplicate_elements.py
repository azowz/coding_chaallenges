from typing import List
def get_duplicate_elements(arr: List[int]) -> List[int]:
    duplicate =[]
    for i in range(len(arr)):
        i +1
        for j in range(i+1,len(arr)):
          if(arr[j] == arr[i]):
             duplicate.append(arr[j])
        j =+ 1

    return duplicate
        
arr = [2, 3, 2, 3]

print (get_duplicate_elements(arr))


