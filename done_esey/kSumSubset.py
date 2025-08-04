from typing import List
def kSumSubset(dateString: str) -> bool:
       # استخراج السنة من سلسلة النص
    year = int(dateString[:4])
    if ( 2020> year > 1824) : 
        return True 
    
    else: return False


d =  '2017-10-21T00:00:00'
print (kSumSubset(d))