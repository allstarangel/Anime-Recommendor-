from media import Media

class Anime(Media):

    class Anime(Media):
        """ A class representing an anime item, inheriting from Media.

        Attributes:
        episode_count (int): The number of episodes in the anime.
        seasons (int): The number of seasons the anime has.
        image_path (str): The path to the image associated with the anime.
        """

    def __init__(self, title, mood, time_commitment, year_released, genre, ratings, episode_count, seasons, image_path):
        # Call the __init__ method of the base class (Media)
        super().__init__(title, mood, time_commitment, year_released, genre, ratings)
        
        # Initialize additional attributes specific to Anime
        self.episode_count = episode_count
        self.seasons = seasons
        self.image_path = image_path



    def display_info(self):
        super().display_info()
        print(f"Episode Count: {self.episode_count}")
        print(f"Seasons: {self.seasons}")

    def display_short_info(self):
        return f"{super().display_short_info()} - Episode Count: {self.episode_count} - Seasons: {self.seasons}"



  

