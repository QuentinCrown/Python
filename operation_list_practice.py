#READ ME
    
    # run this program. you will be given a list of all available seats at the event in the terminal. 
    # you will have to enter the seat that you want. you may get as many seats as there are available.




# seating
available_seats = list(range(1, 21))

# available seats
def display_available_seats():
    if available_seats:
        print("\nAvailable seats: ", available_seats)
    else:
        print("\nAll seats are sold out!")

# process of purchase
def purchase_ticket():
    while True:
        display_available_seats()
        
        try:
            seat_choice = int(input("Please enter the seat number you want to purchase (Enter 0 to finish): "))
        except ValueError:
            print("Invalid input. Please enter a valid seat number.")
            continue
        
        if seat_choice == 0 :
            print("Thank you for your purchase! Enjoy the event.")
            break
        elif seat_choice < 1 or seat_choice > 20:
            print("Invalid seat number. Please choose a seat between 1 and 20.")
        elif seat_choice not in available_seats:
            print(f"Seat {seat_choice} is already sold. Please choose another seat.")
        else:
            # remove selected seat from pool
            available_seats.remove(seat_choice)
            print(f"Seat {seat_choice} has been successfully purchased.")
        
        # all seats sold?
        if not available_seats:
            print("All seats have been sold. No more seats available.")
            break

print("Welcome to the ticket sales system for the event.")
purchase_ticket()
