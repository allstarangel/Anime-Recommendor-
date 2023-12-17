# Anime Recommendation App

This is a simple Anime Recommendation Application that provides anime suggestions based on user input 
i.e mood and time commitment.

## Features
-  Generates random anime recommendations based on mood and time commitment.
-  View anime title and an image of the recommended anime using a graphical user interface (GUI).

## Prerequisites
- Python 3 installed on machine

## Installation
1. Clone the repository:
   - git clone https://github.com/allstarangel/project.git
2. Make sure to install Pillow==8.4.0
  
3. Navigate to the project directory

## Usage 
1. Open a terminal in the project directory

   There are two ways to run this program, via terminal/console or through GUI

   **Running the Main Program:**
     - Open a terminal in the project directory
     - Run th main program:
             python main.py
     - Follow the prompts to enter your mood and time commitment level.
             - VERY IMPORTANT!!!
             - THIS PROGRAM IS CAP SENSITIVE, PLEASE BE SURE TO WRITE YOUR MOOD IN LOWER CASE AS WELL                AS YOUR TIME COMMITMENT.
     - For your mood there are 5 options: 'action' , 'funny', 'adventure', 'sad', 'fantasy'
     - For your time commitment please fully right out either 'long term' or 'short term' in order to          desired results.
     -  Lastly, view the anime recommendation and choose to continue or exit.
  
   **Running the GUI**
     - Open another terminal in the project directory
     - Run the GUI program:
           python gui.py
     - Enter your mood and time commitment level in the GUI (the mood and time commentment behave the          same as the main.py program **THIS IS CAP SENSITIVE** 
     - click the "Generate Recommendation" button to view the anime recommendation and image
  
## Database 

   The 'database.csv' file contains information about various anime titles. Each entry includes         details such as title, mood, time commitment, ratings, and an image path.'

## File Structure
1. 'main.py': The main program that generates anime recommendations based on user input
2. 'gui.py' : The GUI application that provides a user-friendly interface for generating                            recommendations
3. 'anime.py': Defines the 'Anime' class, represnetanint an anime item.
4. 'animedatabase.py': Manages the anime database and includes the 'AnimeDatabase' class.
5. 'media.py': Defines the 'Media' class, representing a generic media item.
6. 'database.csv' : CSV file containing information about anime titles.
  

  
