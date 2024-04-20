import time
import spotipy #python spotify library (makes it easier to access certain things from the API)
from spotipy.oauth2 import SpotifyOAuth 
from flask import Flask, request, url_for, session, redirect
app = Flask(__name__)

#this sets the name for the cookie for the specific session 
app.config['SESSION_COOKIE_NAME'] = 'Spotify Playlist' #cookie name (cookie for security)
app.secret_key = 'fuheuf894y98hi4feifu4' # random value used to stay authorized 
TOKEN_INFO = 'token_info'


@app.route('/')
def login():
    authorize_url = create_spotify_oauth().get_authorized_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirect_page(): 
    session.clear() #clears any previous data from previous session
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code) 
    session[TOKEN_INFO] = token_info
    return redirect(url_for('save_discover_weekly', external = True))

@app.route('/saveDiscoverWeekly')
def save_discover_weekly():

    try:
        token_info = get_token()
    except: 
        print("User not logged in")
        return redirect('/')
    
    return('OAUTH SUCCESSFUL')

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login', external=False))

    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60 #allows 60 seconds of "grace period"
    if(is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
        return token_info

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = "a5312521259a4ee389fe2d99500a171e",
        client_secret = "9b209360584c40009e786d99b40d85c3", 
        redirect_url - url_for('redirect'), _external = True, 
        scope = 'user-library-read playlist-modify-public playlist-modify-private'
        )

app.run(debug=True)