# Given list of artist names with possible duplicates
artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]

# Initialize an empty set to hold unique artist names
unique_artists = set()

# Flag to check if duplicates are found
duplicates_found = False

# Loop through the artist names and add them to the set
for artist in artist_names:
    if artist in unique_artists:
        duplicates_found = True
    unique_artists.add(artist)

# Display the unique artist names
print("Unique artist lineup:", unique_artists)

# Confirm whether duplicates were found
print("Duplicate playlists found:", duplicates_found)
