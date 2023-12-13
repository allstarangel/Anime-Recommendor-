class Media:
    """A class representing a generic media item.

    Attributes:
        title (str): The title of the media item.
        mood (str): The mood associated with the media item.
        time_commitment (str): The time commitment required for the media item.
        year_released (int): The year the media item was released.
        genre (str): The genre of the media item.
        ratings (float): The ratings given to the media item.
    """

    def __init__(self, title, ood, time_commitment, year_released, genre, ratings):

       #Initialize common attributes.

        self.title = title
        self.mood = mood
        self.time_commitment = time_commitment
        self.year_released = year_released
        self.genre = genre
        self.ratings = ratings

    def display_info(self):

        """Display detailed information about the media item."""
 
        print(f"Title: {self.title}")
        print(f"Mood: {self.mood}")
        print(f"Series Length: {self.time_commitment}")
        print(f"Year Released: {self.year_released}")
        print(f"Genre: {self.genre}")
        print(f"Ratings: {self.ratings}")

    def display_short_info(self):

        """Display a concise summary of the media item."""

        print(f"{self.title} - Time Commitment: {self.time_commitment} - Genre: {self.genre} - Ratings: {self.ratings}")

