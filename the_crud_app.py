# main menu
def main_menu():
    """Displays the main menu and prompts the user to select an option."""
    print("\nMenu:")
    while True:
        try:
            print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")

# placeholders
def check():
    """Checks if the customer list file exists and reads its content, otherwise creates a new one."""
    try:
        with open("customer_list.txt", 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []

def save(output):
    """Saves the updated list of customers to the customer_list.txt file."""
    with open("customer_list.txt", 'w') as file:
        for line in output:
            file.write(line)
    print("File updated.")

def create():
    """Creates a new customer entry and appends it to the customer list."""
    customer = check()
    fname = input("Please enter the customer’s first name: ")
    lname = input("Please enter the customer’s last name: ")
    phone = input("Please enter the customer’s phone: ")
    email = input("Please enter the customer’s email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)
    save(customer)
    print(f"Entry for {fname} {lname} created successfully.")

def read():
    """Reads a customer entry by last name."""
    customer = check()
    lname = input("Enter the last name of the customer to search for: ")
    found = False
    for entry in customer:
        if lname.lower() in entry.lower():
            print(f"Entry found: {entry.strip()}")
            found = True
    if not found:
        print(f"No entry found for last name '{lname}'.")

def update():
    """Updates an existing customer's entry in the customer list."""
    customer = check()
    lname = input("Enter the last name of the customer to update: ")
    found = False
    for i, entry in enumerate(customer):
        if lname.lower() in entry.lower():
            print(f"Current entry: {entry.strip()}")
            fname = input("Please enter the new first name (leave blank to keep unchanged): ") or entry.split(", ")[0]
            lname = input("Please enter the new last name (leave blank to keep unchanged): ") or entry.split(", ")[1]
            phone = input("Please enter the new phone (leave blank to keep unchanged): ") or entry.split(", ")[2]
            email = input("Please enter the new email (leave blank to keep unchanged): ") or entry.split(", ")[3].strip()
            new_entry = f"{fname}, {lname}, {phone}, {email}\n"
            customer[i] = new_entry
            save(customer)
            print(f"Updated entry to: {new_entry.strip()}")
            found = True
            break
    if not found:
        print(f"No entry found for last name '{lname}'.")

def delete():
    """Deletes a customer entry from the customer list."""
    customer = check()
    lname = input("Enter the last name of the customer to delete: ")
    found = False
    for i, entry in enumerate(customer):
        if lname.lower() in entry.lower():
            print(f"Entry found: {entry.strip()}")
            confirm = input(f"Are you sure you want to delete this entry? (yes/no): ").lower()
            if confirm == 'yes':
                del customer[i]
                save(customer)
                print("Entry deleted successfully.")
                found = True
                break
    if not found:
        print(f"No entry found for last name '{lname}'.")

# loop and execute
if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            print("Goodbye!")
            break
