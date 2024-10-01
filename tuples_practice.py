def main():
    # tuple of programming classes
    programming_classes = (
        'Intro to Python',
        'Advanced Python',
        'Database Essentials',
        'Web Development Basics',
        'Data Structures in Python',
        'Web Design Fundamentals'
    )

    # loop
    for course in programming_classes:
        print(course)

    # Use the len function to print how many classes are in the tuple
    print(f"\nTotal number of classes: {len(programming_classes)}")

# Run the main function
if __name__ == "__main__":
    main()
