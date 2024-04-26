import time
import spotipy #python spotify library (makes it easier to access certain things from the API)
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect, render_template
app = Flask(__name__)

#this sets the name for the cookie for the specific session 
app.config['SESSION_COOKIE_NAME'] = 'Spotify Playlist' #cookie name (cookie for security)
app.secret_key = 'fuheuf894y98hi4feifu4' # random value used to stay authorized 
TOKEN_INFO = 'token_info'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login.html')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirect_page(): 
    session.clear() #clears any previous data from previous session
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code) 
    session[TOKEN_INFO] = token_info
    return redirect(url_for('save_discover_weekly', _external = True))

@app.route('/saveDiscoverWeekly')
def save_discover_weekly():
    try:
        token_info = get_token()
    except: 
        print("User not logged in")
        return redirect('/')
    
    sp = spotipy.Spotify(auth=token_info['access_token'])
    user_id = sp.current_user()['id']

    current_playlists = sp.current_user_playlists()['items']
    discover_weekly_playlist_id = None
    saved_weekly_playlist_id = None

    for playlist in current_playlists:
        if(playlist['name'] == 'Discover Weekly'):
            discover_weekly_playlist_id = playlist['id']
        if(playlist['name'] == 'Saved Weekly'):
            saved_weekly_playlist_id = playlist['id']
        

    if not discover_weekly_playlist_id:
        return 'Discover Weekly Not Found'
    
    if not saved_weekly_playlist_id:
        new_playlist = sp.user_playlist_create(user_id, 'Saved Weekly', True)
        saved_weekly_playlist_id = new_playlist['id']
    
    #This part reads the existing saved weekly playlist and stores the 
    #URI values
    saved_playlist = sp.playlist_items(saved_weekly_playlist_id)
    saved_song_uris = []
    for song in saved_playlist['items']:
        saved_song_uri = song['track']['uri']
        saved_song_uris.append(saved_song_uri)
    
    discover_weekly_playlist = sp.playlist_items(discover_weekly_playlist_id)
    song_uris = []
    for song in discover_weekly_playlist['items']:
        song_uri = song['track']['uri']
        if song['track']['popularity'] >= 10:
            song_uris.append(song_uri)
    #This part removes the uri of the duplicate songs that already
    #exists in the playlist
        if song['track']['uri'] in saved_song_uris:
            song_uris.remove(song_uri)
        else:
            pass
    #This part checks if the song_uris list is empty, wherein if it's 0,
    #it just returns a message that informs the user that he or she
    #"Already added everything"
    if len(song_uris) == 0:
        return 'Already added everything from this week'
    else:
        sp.user_playlist_add_tracks(user_id, saved_weekly_playlist_id, song_uris, None)
        return render_template('success.html')



def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login', _external=False))

    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60 #allows 60 seconds of "grace period"
    if(is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = "5b86229db55f470d8bb1df43ca85a256",
        client_secret = "28b7911cbfa64d6a9cd35a086118fc5b", 
        redirect_uri = url_for('redirect_page', _external = True), 
        scope = 'user-library-read playlist-modify-public playlist-modify-private'
    )

app.run(host='0.0.0.0', port=10000, debug=True)