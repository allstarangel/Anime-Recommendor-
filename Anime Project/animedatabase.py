# animedatabase.py
import csv
from anime import Anime  # Import the Anime class

class AnimeDatabase:
    def __init__(self, csv_file_path='database.csv'):
        self.anime_entries = []
        self.csv_file_path = csv_file_path
        self.load_data_from_csv()

    def generate_recommendation(self, mood, commitment_level):
        filtered_anime = [a for a in self.anime_entries if anime['mood'] == mood and anime['time_commitment'] == commitment_level]

        if filtered_anime:
            import random
            return random.choice(filtered_anime)
        else:
            return None

    def load_data_from_csv(self):
        self.anime_entries = read_csv()

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


