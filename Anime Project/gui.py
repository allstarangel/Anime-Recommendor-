# gui.py
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from animedatabase import AnimeDatabase

class AnimeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Anime Recommendation App")

        # Create an instance of AnimeDatabase
        self.anime_db = AnimeDatabase()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry widgets for user input
        mood_label = ttk.Label(self.root, text="Enter your mood:")
        self.mood_entry = ttk.Entry(self.root)

        commitment_label = ttk.Label(self.root, text="Enter your commitment level:")
        self.commitment_entry = ttk.Entry(self.root)

        mood_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.mood_entry.grid(row=0, column=1, padx=10, pady=10)

        commitment_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.commitment_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button to generate recommendation
        generate_button = ttk.Button(self.root, text="Generate Recommendation", command=self.generate_recommendation)
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Display area for recommendation and image
        self.recommendation_label = ttk.Label(self.root, text="Recommended Anime:")
        self.recommendation_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.image_label = ttk.Label(self.root)
        self.image_label.grid(row=4, column=0, columnspan=2, pady=10)

    def generate_recommendation(self):
        user_mood = self.mood_entry.get()
        user_commitment_level = self.commitment_entry.get()

        recommendation = self.anime_db.generate_recommendation(user_mood, user_commitment_level, None)  # Replace None with the actual value for display_output

        if recommendation:
            self.recommendation_label.config(text=f"Recommended Anime: {recommendation.title}")
            self.display_image(recommendation.image_path)
        else:
            self.recommendation_label.config(text="No matching anime found in the database.")
            self.image_label.config(image=None)
    
    def display_image(self, image_path):
        abs_image_path = os.path.abspath(image_path)
        abs_image_path = os.path.join(os.path.dirname(__file__), abs_image_path)

        try:
            img = Image.open(abs_image_path)
            img = img.resize((400, 600), Image.NEAREST)
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img  # Keep a reference to prevent garbage collection
        except FileNotFoundError:
            print(f"Error loading image: {abs_image_path}")
    def display_recommendation(self, recommendation):
         if recommendation:
            text = f"Recommended Anime: {recommendation.title}\n"
            text += f"Genre: {recommendation.genre}\n"
            text += f"Ratings: {recommendation.ratings}\n"
            text += f"Mood: {recommendation.mood}\n"
            text += f"Time Commitment: {recommendation.time_commitment}\n"
            text += f"Year Released: {recommendation.year_released}\n"

            if recommendation.episode_count is not None:
                text += f"Episode Count: {recommendation.episode_count}\n"

            if recommendation.seasons is not None:
                text += f"Seasons: {recommendation.seasons}\n"

            self.recommendation_label.config(text=text)
            self.display_image(recommendation.image_path)
         else:
                self.recommendation_label.config(text="No matching anime found in the database.")
                self.image_label.config(image=None)




def main():
    root = tk.Tk()
    app = AnimeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

