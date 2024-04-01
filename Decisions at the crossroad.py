#Task 1: Code Correction 


number = float(input("Enter a number: ")) #Needs float for comparison

if number > 0:
    print("The number is positive.")
elif number == 0:  # Use == for comparison
    print("The number is zero.")
else:  # Doesnt need condition
    print("The number is negative.")
