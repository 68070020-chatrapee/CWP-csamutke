num1 = int(input("Enter the first number :\n"))
num2 = int(input("Enter the second number :\n"))
mul = num1 * num2
print(str(num1) + " x " + str(num2) + " = " + str(mul))
if mul > 0:
    print("This number is positive.")
elif mul < 0:
    print("This number is negative.")
else:
    print("This number is both positive and negative.")