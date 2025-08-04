from typing import List
def convertPercent(percentage: str) -> float:
    num = int(percentage[:-1]) / 100 
    return num

print(convertPercent("34%"))