# READ ME

# run this program. you will then be asked to enter each persons name in the terminal. please do so.
# then, the program will then display the list of names and then that same list reversed.

names = []

# name range 
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

# bubble sort essentially organizes the list alphabetically 
for i in range(len(names)):
    for j in range(0, len(names) - i - 1):
        if names[j] > names[j + 1]:
            # Swap if the current name is greater than the next name
            names[j], names[j + 1] = names[j + 1], names[j]

# sorted list
print("\nSorted list of names:")
print(names)

# reverse the sorted list
names.reverse()

print("\nReversed list of names:")
print(names)
