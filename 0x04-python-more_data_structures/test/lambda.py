#!/usr/bin/python3

C = [39.2, 36.5, 37.3, 38, 37.8]
# fahrenheit -> float(9)/5)*x + 32
# Calculus ->  (float(5)/9)*(x-32)
F = list(map(lambda x: (float(9)/5) * x + 32, C))
C = list(map(lambda x: (float(5)/9) * (x-32), F))
print(F)
print(C)
