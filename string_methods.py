# Python String Methods Practice

# Use the capitalize() method to capitalize the first letter of the string
string1 = "python"
print(string1.capitalize())

# Use the center() method to center the string in a string of specified width
string2 = "python"
print(string2.center(10))

# Use the endswith() method to check if the string ends with a specified substring
string3 = "python"
print(string3.endswith("on"))

# Use the find() method to find the first occurrence of a substring in the string
string4 = "python"
print(string4.find("th"))

# Use the isalnum() method to check if all characters in the string are alphanumeric
string5 = "python3"
print(string5.isalnum())

# Use the isalpha() method to check if all characters in the string are alphabetic
string6 = "python"
print(string6.isalpha())

# Use the islower() method to check if all characters in the string are lowercase
string7 = "python"
print(string7.islower())

# Use the isspace() method to check if all characters in the string are whitespaces
string8 = " "
print(string8.isspace())

# Use the isupper() method to check if all characters in the string are uppercase
string9 = "PYTHON"
print(string9.isupper())

# Use the join() method to join elements of an iterable with the string as the separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
print(separator.join(iterable1))

# Use the lower() method to convert all characters in the string to lowercase
string10 = "PYTHON"
print(string10.lower())

# Use the lstrip() method to remove leading characters (spaces by default)
string11 = " python"
print(string11.lstrip())

# Use the rstrip() method to remove trailing characters (spaces by default)
string12 = "python "
print(string12.rstrip())

# Use the replace() method to replace all occurrences of a substring with another substring
string13 = "I love python"
print(string13.replace("python", "snake"))

# Use the rfind() method to find the highest index of a substring
string14 = "python"
print(string14.rfind("n"))

# Use the split() method to split the string at a specified separator
string15 = "python-is-fun"
print(string15.split("-"))

# Use the startswith() method to check if the string starts with a specified substring
string16 = "python"
print(string16.startswith("py"))

# Use the strip() method to remove both leading and trailing characters (spaces by default)
string17 = " python "
print(string17.strip())

# Use the swapcase() method to swap the case of all characters in the string
string18 = "Python"
print(string18.swapcase())

# Use the title() method to convert the first character of each word to uppercase
string19 = "python is fun"
print(string19.title())

# Use the upper() method to convert all characters in the string to uppercase
string20 = "python"
print(string20.upper())
