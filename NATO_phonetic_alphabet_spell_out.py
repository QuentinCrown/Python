# NATO phonetic alphabet dictionary
nato_alphabet = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta",
    "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel",
    "I": "India", "J": "Juliette", "K": "Kilo", "L": "Lima",
    "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
    "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu"
}

def main():

    word = ("") # enter your word between the ""

    # go through each letter
    for letter in word:
        upper_letter = letter.upper()
        if upper_letter in nato_alphabet:
            print(f"{letter}: {nato_alphabet[upper_letter]}")
        else:
            print(f"{letter}: Not a valid letter in the NATO alphabet")

# run main
if __name__ == "__main__":
    main()
