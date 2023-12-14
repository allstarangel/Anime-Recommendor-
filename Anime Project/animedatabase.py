# animedatabase.py
import csv
from anime import Anime  # Import the Anime class

class AnimeDatabase:
    def __init__(self, csv_file_path='database.csv'):
        self.anime_entries = []
        self.csv_file_path = csv_file_path
        self.load_data_from_csv()

    def generate_recommendation(self, mood, commitment_level):
        mood = mood.lower()  # Convert user input to lowercase
        commitment_level = commitment_level.lower()  # Convert user input to lowercase

        filtered_anime = [anime for anime in self.anime_entries if anime.mood.lower() == mood and anime.time_commitment.lower() == commitment_level]

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


