import csv
from anime import Anime

class AnimeDatabase:
    def __init__(self, csv_file_path='database.csv'):
        self.anime_entries = []
        self.csv_file_path = csv_file_path
        self.load_data_from_csv()

    def generate_recommendation(self, mood, time_commitment):
        filtered_anime = [anime for anime in self.anime_entries if anime.mood == mood and anime.time_commitment == commitment_level]

        if filtered_anime:
            import random
            return random.choice(filtered_anime)
        else:
            return None

    def load_data_from_csv(self):
        self.anime_entries = read_csv() 

def read_csv():
    file_path = 'database.csv'
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                anime = Anime(
                    row['title'],
                    row['mood'],
                    row['time_commitment'],
                    int(row['year_released']),
                    row['genre'],
                    row['ratings'],
                    int(row['episode_count'])
                )
                self.anime_entries.append(anime)
    except FileNotFoundError:
        print(f"CSV file '{file_path}' not found.")
    return data