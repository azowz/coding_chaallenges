from typing import List
def numbers_range(number: int) -> str:
    result = ""
    for num in range(number):
        result += str(num) + " "

    result += str(number)    
    return result 

print(numbers_range(5))
#creat vlaeu uot loop 
    #loop end befor laste number 
    #if you want add value for prevos value +=