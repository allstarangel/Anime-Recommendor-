# animedatabase.py
import csv
from anime import Anime  # Import the Anime class


class AnimeDatabase:
    def __init__(self, csv_file_path='database.csv'):
        self.anime_entries = []
        self.csv_file_path = csv_file_path
        self.load_data_from_csv()

    def generate_recommendation(self, mood, commitment_level, display_output):
        # Print debug information about the anime entries
        print("Debug Information:")
        for anime in self.anime_entries:
            print(f"Title: {anime.title}, Mood: {anime.mood}, Time Commitment: {anime.time_commitment}")

        # Filter anime based on user input
        filtered_anime = [
            anime for anime in self.anime_entries
            if anime and anime.mood and anime.time_commitment
            and mood.lower() in anime.mood.lower()
            and anime.time_commitment.lower() == commitment_level
        ]

        # Print filtered anime for debugging
        print("\nFiltered Anime:")
        for anime in filtered_anime:
            print(f"Title: {anime.title}, Mood: {anime.mood}, Time Commitment: {anime.time_commitment}")

        if filtered_anime:
            import random
            return random.choice(filtered_anime)
        else:
            return None


    def load_data_from_csv(self):
        data = read_csv()
        for row in data[1:]:  # Start from the second row to skip the header
            try:
                anime = Anime(
                    row['Title'],
                    row['Mood'],
                    row['Time Commitment'],
                    int(row['Year Released']) if row['Year Released'] else None,
                    row['Genre'],
                    row['Ratings'],
                    int(row['Episode Count']) if row['Episode Count'] else None,
                    int(row['Seasons']) if row['Seasons'] else None
                )
                self.anime_entries.append(anime)
            except ValueError as e:
                print(f"Error processing row: {row}. {e}")



# Add the read_csv function
def read_csv():
    file_path = 'database.csv'
    data = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"CSV file '{file_path}' not found.")
    return data


