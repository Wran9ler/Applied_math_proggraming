"""
Write a program that allows the user to specify the number of iterations n
 used in this approximation and that displays the resulting value with 5 decimal accuracy
"""

n = int(input())
pi = 0

for i in range(1, n+1):
    term = (-1)**(i+1) / (2*i - 1)
    pi += 4 * term

print(f"{pi:.5f}")

