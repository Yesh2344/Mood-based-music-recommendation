import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from utils import get_mood_playlist, get_top_tracks

# Download necessary NLTK data
nltk.download('vader_lexicon')

# Load environment variables
load_dotenv()

# Set up Spotify client
client_credentials_manager = SpotifyClientCredentials(
    client_id=os.getenv('SPOTIFY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def analyze_mood(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    
    if sentiment['compound'] >= 0.05:
        return 'positive'
    elif sentiment['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

def recommend_music(mood):
    playlist_id = get_mood_playlist(sp, mood)
    if playlist_id:
        tracks = get_top_tracks(sp, playlist_id)
        return tracks
    return None

def main():
    print("Welcome to the Mood-Based Music Recommender!")
    print("Tell me how you're feeling, and I'll recommend some music for you.")
    
    while True:
        user_input = input("\nHow are you feeling? (or type 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            print("Thank you for using the Mood-Based Music Recommender. Goodbye!")
            break
        
        mood = analyze_mood(user_input)
        print(f"\nBased on your input, your current mood seems to be: {mood}")
        
        recommendations = recommend_music(mood)
        
        if recommendations:
            print("\nHere are some song recommendations for you:")
            for i, track in enumerate(recommendations, 1):
                print(f"{i}. {track['name']} by {track['artists'][0]['name']}")
        else:
            print("\nSorry, I couldn't find any recommendations for your current mood.")

if __name__ == "__main__":
    main()