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
    
    # Ask the user for display preference
    display_output = input("Would you want a long display or short (e.g., 'short' or 'long'): ").lower()

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
    
    # Ask user if they want to continue generating recommendations
    user_input = input("Do you want another recommendation? (yes/no): ").lower()
    if user_input != 'yes':
        break

if __name__ == "__main__":
    main()



