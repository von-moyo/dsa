import string
from typing import List


def generate(numRows: int) -> List[List[int]]:
    triangle = []
    for i in range(numRows):
        row = [1] * (1 + i)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle


print(generate(5))


def reverseString(word: string) -> string:
    array = []
    n = len(word)
    for i in range(n-1,-1,-1):
        array.append(word[i])
    return ''.join(array)


print(reverseString("fortune"))
