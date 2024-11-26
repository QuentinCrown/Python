# generator function
def two_letter_combinations(char_list):

    # first loop
    for char1 in char_list:
        # second loop
        for char2 in char_list:
            # Use yield to return each two-letter combination
            yield char1 + char2

# main
if __name__ == "__main__":
    # characters
    characters = ['x', 'y', 'z', 'm', 'n']
    
    # call and print
    print("All possible two-letter combinations:")
    for combination in two_letter_combinations(characters):
        print(combination)
