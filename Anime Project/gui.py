# gui.py
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
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

        recommendation = self.anime_db.generate_recommendation(user_mood, user_commitment_level)

        if recommendation:
            self.recommendation_label.config(text=f"Recommended Anime: {recommendation.title}")
            self.display_image(recommendation.image_path)
        else:
            self.recommendation_label.config(text="No matching anime found in the database.")
            self.image_label.config(image=None)

    def display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((200, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.image_label.config(image=img)
        self.image_label.image = img  # Keep a reference to prevent garbage collection


def main():
    root = tk.Tk()
    app = AnimeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()