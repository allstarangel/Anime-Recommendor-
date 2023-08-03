#animedatabase.py

import csv
from anime import Anime as  an  

class AnimeDatabase:
    def __init__(self, csv_file_path='database.csv'):
        self.anime_entries = []
        self.csv_file_path = csv_file_path
        self.load_data_from_csv()

    def generate_recommendation(self, mood, commitment_level):
        filtered_anime = [anime for anime in self.anime_entries if anime.mood == mood and anime.time_commitment == commitment_level]

        if filtered_anime:
            import random
            return random.choice(filtered_anime)
        else:
            return None

    def load_data_from_csv(self):
        try:
            with open(self.csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    anime = an(row)
                    self.anime_entries.append(anime)
        except FileNotFoundError:
            print(f"CSV file '{self.csv_file_path}' not found. Creating a new one.")
