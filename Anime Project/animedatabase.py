# animedatabase.py
import csv
from anime import Anime

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
        file_path = 'database.csv'
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                print(reader.fieldnames)

                for row in reader:
                    print(row)
                    anime = Anime(
                                row['title'],
                                row['mood'],
                                row['time commitment'],
                                int(row['year released']),
                                row['genre'],
                                row['ratings'],
                                int(row['episode count'])
                                )
                    self.anime_entries.append(anime)
        except FileNotFoundError:
            print(f"CSV file '{file_path}' not found.")

