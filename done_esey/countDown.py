from typing import List

def countDown(number: int) -> str:
    c = ''
    for i in range(number, -1, -1):
        c += str(i) + ' '
    return c.strip()

f = 20

print(countDown(f))
