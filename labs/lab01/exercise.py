def add_with_print(a, b):
    result = a + b
    print(result)  # shows the number

def add_with_return(a, b):
    result = a + b
    return result  # gives the number back

x = add_with_print(5, 3)
print(f"x contains: {x}")

y = add_with_return(5, 3)
print(f"y contains: {y}")

print(y + 1)
print(x + 1)

