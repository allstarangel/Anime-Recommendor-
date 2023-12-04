#main.py

from animedatabase import AnimeDatabase

def get_user_input():
    """Get user input for mood and commitment level."""
    mood = input("Enter your mood (e.g., happy, sad, adventurous): ")
    commitment_level = input("Enter your commitment level (e.g., short term, long term): ")
    return mood, commitment_level

def main():
    # Create an instance of AnimeDatabase
    anime_db = AnimeDatabase()

    # Get user preferences
    user_mood, user_commitment_level = get_user_input()

    # Generate anime recommendation based on user preferences
    recommendation = anime_db.generate_recommendation(user_mood, user_commitment_level)

    # Display the recommendation
    if recommendation:
        print("\nRecommended Anime:")
        print(recommendation.display_short_info())
    else:
        print("\nNo matching anime found in the database.")

if __name__ == "__main__":
    main()

