def main():
    # starting list
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", 
                   "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]

    # show list
    print("Top Performing Artists:")
    for i, artist in enumerate(top_artists, start=1):
        print(f"{i}. {artist}")
    
    # start replacement
    modify_artist_list(top_artists)
    
    # modified list
    print("\nUpdated List of Top Performing Artists:")
    for i, artist in enumerate(top_artists, start=1):
        print(f"{i}. {artist}")

def modify_artist_list(artists):
    try:
        # spot and artist
        index = int(input("Enter the position (1-10) of the artist you want to replace: ")) - 1
        new_artist = input("Enter the new artist's name: ").strip()

        # Replace the artist at spot
        artists[index] = new_artist
        print(f"Artist at position {index + 1} has been replaced with {new_artist}.")

    except (ValueError, IndexError):
        # errors
        print("An input error occurred. Please enter a valid position between 1 and 10.")

# run
if __name__ == "__main__":
    main()
