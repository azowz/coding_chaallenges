from typing import List
def reverse_case(strParam: str) -> str:
  i = len (strParam)
  reverse = ""
  while  i == 0 :
    reverse = reverse + strParam[i]
    i=-1
    
  return reverse 


print(reverse_case("TeSt"))
