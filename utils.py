def get_mood_playlist(sp, mood):
    # You can customize these playlist IDs or search for playlists dynamically
    mood_playlists = {
        'positive': '37i9dQZF1DX3rxVfibe1L0',  # "Happy Hits!" playlist
        'negative': '37i9dQZF1DX3YSRoSdA634',  # "Life Sucks" playlist
        'neutral': '37i9dQZF1DX1s9knjP51Oa',   # "Calm Vibes" playlist
    }
    return mood_playlists.get(mood)

def get_top_tracks(sp, playlist_id, limit=5):
    results = sp.playlist_tracks(playlist_id, limit=limit)
    return [item['track'] for item in results['items']]