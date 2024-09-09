# Initial number of bottles
initial_bottles = 99

bottles = initial_bottles

# While loop to handle the verses
while bottles > 0:
    if bottles > 1:
        # more than one bottle verse
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} {'bottle' if bottles - 1 == 1 else 'bottles'} of beer on the wall.\n")
    else:
        # one bottle verse
        print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")
    
    # time to end this
    bottles -= 1

# final verse
print("No more bottles of beer on the wall, no more bottles of beer.")
print(f"Go to the store and buy some more, {initial_bottles} bottles of beer on the wall.")
