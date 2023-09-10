# Input an integer from the user
num = int(input("Enter an integer: "))

# Check if the input is a non-negative integer
if num >= 0:
    binary_representation = bin(num)  # Convert to binary
    binary_representation = binary_representation[2:]  # Remove the '0b' prefix

    print(f"The binary representation of {num} is: {binary_representation}")
else:
    print("Please enter a non-negative integer.")
