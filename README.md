# Mood-Based Music Recommender

This project is a Python-based application that recommends music based on the user's current mood. It uses natural language processing to analyze user input and suggests songs from Spotify playlists that match the detected mood.

## Features

- Sentiment analysis of user input to determine mood
- Integration with Spotify API to fetch mood-based playlists
- Recommendation of top tracks from mood-appropriate playlists

## Prerequisites

- Python 3.7+
- Spotify Developer account

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/mood-based-music-recommender.git
   cd mood-based-music-recommender
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Spotify API credentials:
   ```
   SPOTIFY_CLIENT_ID=your_client_id_here
   SPOTIFY_CLIENT_SECRET=your_client_secret_here
   ```

## Usage

Run the script:
```
python mood_music_recommender.py
```

Follow the prompts to enter your current mood. The application will analyze your input and recommend songs based on the detected sentiment.

## How to obtain Spotify Client ID and Client Secret

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Log in with your Spotify account (create one if you don't have it)
3. Click on "Create an App"
4. Fill in the app name and description, then click "Create"
5. In your app's dashboard, you'll find your Client ID and Client Secret
6. Copy these credentials to your `.env` file

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

@YeswanthSoma All Copyrights Reserved


## Contact

Email:yeswanthsoma83@gmail.com
