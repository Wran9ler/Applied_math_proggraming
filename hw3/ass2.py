"""
Write a program that accepts 2 positive integers as inputs and outputs the greatest common divisor of the two. 
"""

a, b = map(int, input().split())

i = 1
gcd = 1

while i <= min(a, b):
    if a % i == 0 and b % i == 0:
        gcd = i
    i += 1

print(f"{gcd}")

