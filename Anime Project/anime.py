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


    def calculate_watch_time(self):
        """Calculate the total watch time 
        based on episode count and time commitment.
        """

        # Determine if it's short term or long term based on the number of seasons
        if "season" in self.time_commitment.lower() and "long term" not in self.time_commitment.lower():
            # If there are more than 2 seasons, consider it long term
            num_seasons = int(self.time_commitment.lower().split("season")[0].strip())
            if num_seasons > 2:
                time_commitment_category = "Long Term"
            else:
                time_commitment_category = "Short Term"
        else:
            # If "long term" is explicitly mentioned, consider it long term
            time_commitment_category = "Long Term" if "long term" in self.time_commitment.lower() else "Short Term"

        # Calculate watch time based on time commitment category and episode count
        if time_commitment_category == "Short Term":
            watch_time = self.episode_count * num_seasons
        else:
            watch_time = self.episode_count * 2 * num_seasons  # Assume longer time for long-term commitments

        return f"Estimated Watch Time: {watch_time} episodes"

  

