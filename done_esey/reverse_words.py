
from typing import List
def reverse_words(str1: str, str2: str) -> str:
    reverse = str2+", " + str1
    return reverse 

print(reverse_words(str1 = 'test',str2 = 'one'))