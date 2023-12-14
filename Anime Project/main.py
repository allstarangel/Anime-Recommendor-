from animedatabase import AnimeDatabase

def get_user_input():
    """Get user input for mood and commitment level."""
    mood = input("Enter your mood (e.g., action, sad, adventurous): ")
    commitment_level = input("Enter your commitment level (e.g., short term, long term): ")
    display_output = input("Would you want a short or long display? (pick either: 'short' or 'long': )")
    return mood, commitment_level, display_output

def main():
    while True:
        # Create an instance of AnimeDatabase
        anime_db = AnimeDatabase() 

        # Get user preferences
        user_mood, user_commitment_level, display_output = get_user_input()

        # Generate anime recommendation based on user preferences
        recommendation = anime_db.generate_recommendation(user_mood, user_commitment_level, display_output)

        # Display the recommendation
        if recommendation:
            print("\nRecommended Anime:")
            if display_output == 'short':
                print(recommendation.display_short_info())
            else:
                print(recommendation.display_info())
        else:
            print("\nNo matching anime found in the database.")

        # Ask the user if they want to continue
        user_input = input("Do you want another recommendation? (yes/no): ").lower()
        if user_input != 'yes':
            break  # This break statement should be aligned with the while loop

if __name__ == "__main__":
    main()



