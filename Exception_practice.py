def square_number():
    while True:
        try:
        
            number = ("") # enter you number between the ""
            number = int(number)
            squared_number = number ** 2
            print(f"The square of {number} is {squared_number}.") # result
            break
        except ValueError:
            # if not valid number
            print("Invalid input. Please enter a valid number.")

# Run the function
square_number()
