from typing import List
def divisible_by_five(num: int) -> bool:
   remainder =num % 5
   if(remainder == 0 ):
      return True
   else :
      return False  
   

num =48 
print (divisible_by_five(num ))