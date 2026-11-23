# Lab 01 Exercise 5: Triangle Checker
def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(f"{is_valid_triangle(3, 4, 5)}")
print(f"{is_valid_triangle(1, 2, 3)}")