# Initialize the number with a non-zero value
number = None
# Start the while loop
while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    # Perform an action with the number
    if number != 0:
        print(f"You entered {number}.")
    else:
        print("Exiting the program.")

# Outside the loop
print("Program ended.")


