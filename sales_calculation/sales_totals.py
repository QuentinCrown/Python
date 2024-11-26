def main():
    
    total = 0.0
    count = 0

    try:
        # open file
        with open('sales_totals.txt', 'r') as file:
            print("Sales Totals:")
            print("-------------")

            # loop
            for line in file:
                try:
                    # float
                    sales = float(line.strip())
                    # running total
                    total += sales
                    # Incrementing
                    count += 1
                    # formatted number
                    print(f"${sales:,.2f}")
                except ValueError:
                    # invalid lines
                    print(f"Skipping invalid line: {line.strip()}")

        # loop, display total, count, and average
        if count > 0:
            average = total / count
            print("\nSummary:")
            print(f"Total Sales: ${total:,.2f}")
            print(f"Number of Entries: {count}")
            print(f"Average Sale: ${average:,.2f}")
        else:
            print("No valid sales data found.")

    except FileNotFoundError:
        print(f"Error: The file 'sales_totals.txt' does not exist in the current directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
