n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print("Choose one of the following:")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
ch = int(input("Enter your choice: "))
if ch == 1:
    print(f"Result: {n1+n2}")
elif ch == 2:
    print(f"Result: {n1-n2}")
elif ch == 3:
    print(f"Result: {n1*n2}")
elif ch == 4:
    if n2==0:
        print("Division by zero is not possible!")
    else:
        print(f"Result: {n1/n2}")
else:
    print("Invalid choice")
