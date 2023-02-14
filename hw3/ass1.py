"""

Write a program that takes the length of three sides of a triangle as input.
The output of the program should indicate whether the triangle is rectangular or not.

"""

a, b, c = map(int, input().split())

if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
    print("Yes")
else:
    print("No")

