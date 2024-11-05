def main():
    # start list
    flowers = []

    # enter flower names
    print("Enter the names of flowers. Type 'done' when you're finished.")
    while True:
        flower = input("Flower name: ").strip()
        if flower.lower() == "done":
            break
        if flower:  # no empty entries
            flowers.append(flower)

    # Sort list
    flowers.sort()

    # Print sorted list
    print("\nHere are the flowers you entered:")
    for i, flower in enumerate(flowers, start=1):
        print(f"{i}. {flower}")

    # specific flower
    search_flower = input("\nEnter the name of the flower you'd like to search for: ").strip()
    if search_flower in flowers:
        print(f"{search_flower} is in the list!")
    else:
        print(f"{search_flower} was not found in the list.")

    # Access that flower using number
    while True:
        try:
            index = int(input("\nEnter the number of the flower you want to access: ")) - 1
            # flower name
            print(f"The flower at position {index + 1} is {flowers[index]}.")
            break  # good = done

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except IndexError:
            print("Invalid index. Please enter a number within the range of the list.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run
if __name__ == "__main__":
    main()
