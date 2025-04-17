def print_ones_digit(num):
    # Get the ones digit using modulo
    ones_digit = abs(num) % 10
    print(f"The ones digit is {ones_digit}")

def main():
    # Get user input
    number = int(input("Enter a number: "))
    # Call the function
    print_ones_digit(number)

# Run the program
main()
