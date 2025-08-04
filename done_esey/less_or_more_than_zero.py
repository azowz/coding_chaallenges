from typing import List
def less_or_more_than_zero(number: int) -> str:
    if (number > 0):
        return 'Greater than zero'
    if  (number == 0) :
        return 'Equal to zero'
    else :
        return 'Less than zero'
