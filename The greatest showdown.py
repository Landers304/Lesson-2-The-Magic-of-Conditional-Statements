#Task1: Identify the Greatest


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)




#Task2: Identify the Smallest


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print("The largest number is:", largest)
print("The smallest number is:", smallest)




#Task3: Equality Chec Check


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

if num1 < num2 and num1 < num3:
    smallest = num1
elif num2 < num1 and num2 < num3:
    smallest = num2
else:
    smallest = num3

if num1 == num2 and num1 == num3:
    print("All numbers are equal.")
elif num1 == num2:
    print(f"The numbers {num1} and {num2} are equal.")
elif num1 == num3:
    print(f"The numbers {num1} and {num3} are equal.")
elif num2 == num3:
    print(f"The numbers {num2} and {num3} are equal.")
else:
    print("No two numbers are equal.")

print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")
