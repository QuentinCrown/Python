import re

def main():
    while True:
        # enter password
        password = input("Enter a password: ")

        # Validate the password 
        if not (8 <= len(password) <= 20):
            print("Password must be between 8 and 20 characters long.")
            continue
        if not re.search(r"[A-Z]", password):
            print("Password must contain at least one uppercase letter.")
            continue
        if not re.search(r"[a-z]", password):
            print("Password must contain at least one lowercase letter.")
            continue
        if not re.search(r"[0-9]", password):
            print("Password must contain at least one number.")
            continue
        if not re.search(r"[!@#$%&*]", password):
            print("Password must contain at least one symbol from !@#$%&*.")
            continue

        # If good, confirm the password
        try:
            confirm_password = input("Re-enter your password for confirmation: ")
            if password == confirm_password:
                print("Password successfully set!")
                break
            else:
                print("Passwords do not match. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

# Run 
if __name__ == "__main__":
    main()
