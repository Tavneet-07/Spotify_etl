from dotenv import load_dotenv
import os
import base64
import requests
from requests import post
import json
from requests import get
from datetime import datetime, timedelta
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
print("client_ID=",client_id, "client_secret=",client_secret)
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "user-read-recently-played"
    }
    result = post(url, headers=headers, data=data)
    if result.status_code == 200:
        json_result = json.loads(result.content)
        Token = json_result["access_token"]
        return Token
        print(Token)
    else:
        print("Error", result.status_code, result.text)
        return None
def get_auth_header(Token):
    return {"Authorization": "Bearer " + Token}
def search_for_artist(Token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(Token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    
    if len(json_result) == 0:
        print("No artist with this name exists")
        return None
    
    return json_result[0]
def get_songs_by_artist(Token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(Token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    
    return json_result
def get_valid_token():
    global access_token
    global token_expiration_time



    # Check if we have a valid token or need to get a new one
    if not access_token or datetime.now() >= token_expiration_time:
        access_token = get_token()
        if access_token:
            # Set token expiration time to 1 hour from now
            token_expiration_time = datetime.now() + timedelta(hours=1)
        else:
            raise Exception("Failed to retrieve a valid token")
    return access_token
access_token = None
token_expiration_time = datetime.now()  # Initialize token expiration time to be in the past
Token = get_valid_token()
# Main program
if __name__ == "__main__":
    result = search_for_artist(Token, "Ed sheeran")
    print("Token=",Token)
    print(result["name"])
    artist_id = result["id"]
    print("artist ID =", artist_id)
    songs = get_songs_by_artist(Token, artist_id)
    for idx, song in enumerate(songs):
        print(f"{idx + 1}. {song['name']}")