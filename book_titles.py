def main():
    # book titles
    book_titles = []
    
    # 10 of them
    while len(book_titles) < 10:
        title = input("Enter a book title: ").title()  # Capitalize
        book_titles.append(title)
    
    # sorted list
    sorted_titles = sorted(book_titles)
    
    # Display
    print("\nHere are the book titles in alphabetical order:")
    for title in sorted_titles:
        print(title)

# Run
if __name__ == "__main__":
    main()
