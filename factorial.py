from typing import List
def factorial(number: int) -> int:
    result = 1
    for i in range(2, number + 1):
            result *= i
        
    return result



print (factorial (10))