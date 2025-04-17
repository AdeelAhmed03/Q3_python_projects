# print multiple 

def print_multiple(message: str, repeats: int):
    print("Here are the divisors of", message)
    for i in range(repeats):
        curr_divisor = i + 1
        if repeats % curr_divisor == 0:
            print(curr_divisor)

def main():
    num = int(input("Enter a number: "))
    print_multiple(num)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()