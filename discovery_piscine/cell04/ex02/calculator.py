a = int(input("Give me the first number: "))
b = int(input("Give me the second number: "))
print("Thank you!")
division = a /b
if division.is_integer():
    division = int(division)

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} / {b} = {division}")
print(f"{a} * {b} = {a * b}")