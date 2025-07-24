print("Simple Calculator")
print("Choose operation: +  -  *  /")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b == 0:
        print("Error: Cannot divide by zero.")
    else:
        print("Result:", a / b)
else:
    print("Invalid operation.")
