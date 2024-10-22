def main():
    # Example string
    example_string = "Hello, Python programmers!"
    
    # Iterate through the string and print each character
    print("Iterating through the string:")
    for char in example_string:
        print(char, end=" ")
    
    # Find and print the character with the minimum ASCII value in the string
    print("\n\nCharacter with the minimum ASCII value:")
    print(min(example_string))
    
    # Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:")
    print(max(example_string))
    
    # Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    print(example_string.index('o'))
    
    # Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    char_list = list(example_string)
    print(char_list)
    
    # Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    print(example_string.count('o'))

main()
