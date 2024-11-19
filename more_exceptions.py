# exception class
class NotNumericError(Exception):
    """Exception raised for inputs that are not numeric."""
    def __init__(self, input_value):
        super().__init__(f"Invalid input: '{input_value}' is not a numeric value.")

# valid number please
def get_number():
    while True: 
        try:
            user_input = input("Enter a number: ")
            if not user_input.isnumeric():
                raise NotNumericError(user_input)  # invalid input
            number = int(user_input) 
        except NotNumericError as e:
            print(f"Error: {e}") 
        else:
            print(f"Valid input! You entered the number: {number}")
            break  # exit loop w/ valid input
        finally:
            print("Attempt to validate input completed.") 
    print("Program execution complete.")

# run 
if __name__ == "__main__":
    get_number()
