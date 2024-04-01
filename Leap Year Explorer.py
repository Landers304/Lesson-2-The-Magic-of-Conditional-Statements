#Task1: Leap Year Checker


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 # If the year is divisible by 4 and not by 100, or divisible by 400, it's a leap year   
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
