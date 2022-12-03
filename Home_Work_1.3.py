a = [1, 1, 2, 3, 4, 4, 4]


b = [i for i in a if a.count(i) == 1]
print(b)
import math

n = 5
print(f'- при d = {n}, {chr(960)} = {str(math.pi)[:n+2]}')