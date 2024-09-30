def factorial(n):
    # base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # recursive step: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

def main():
    while True:
        try:
            
            number = int(" 12") #enter a non-negative number
            if number < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # call it
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")
 # run main
if __name__ == "__main__":
    main()
