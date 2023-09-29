import pandas as pd 
import requests
from datetime import datetime
import datetime
import Token

USER_ID = "31jzp3jbehu6ne4qcrxrcanyrfb4" 
TOKEN = Token.Token

# Creating a function to be used in other Python files
def return_dataframe(playlist_url):  # Add playlist_url as a parameter
    input_variables = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN),
        "scope": "user-read-recently-played"
    }
     
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=2)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
    artist_id= playlist_url.split("/")[-2]
    playlist_tracks_url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"

    
    r = requests.get(playlist_tracks_url, headers=input_variables)

    if r.status_code != 200:
        print("Failed to retrieve data from Spotify API.",r.status_code)
        return None

    data = r.json()
    # df1=pd.DataFrame(data)
    # print(df1)
    if "tracks" not in data:
        print("No 'items' key found in the response. Check if the playlist URL is correct.")
        return None
    # for idx, song in enumerate(songs):
    #     print(f"{idx + 1}. {song['name']}")

    song_names = []
    artist_names = []
    for tracks in data["tracks"]:
        
        song_names.append(tracks["name"])
        artist_names.append(tracks["artists"][0]["name"])

    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names
    }

    song_df = pd.DataFrame(song_dict, columns=["song_name", "artist_name"])
    return song_df

playlist_url = "https://api.spotify.com/v1/artists/6eUKZXaKkcviH0Ku9w2n3V/top-tracks?country=US"  ## tis url will return the playlist of user name= tavneet whose id is (31jzp3jbehu6ne4qcrxrcanyrfb4)
df = return_dataframe(playlist_url)
if df is not None:
    print(df)




# import pandas as pd 
# import requests
# from datetime import datetime
# import datetime


# USER_ID = "Tavneet" 
# TOKEN = "BQAG5EFVCF6FUYwbjYCPE2zf1Ci_-4amccm6m81Dm69hDBsNsx6_uaNcMNJG0xG253rYzxVMhhWrMEcqq4h3kh0Oiu0-Vdqpecd0-jRfBewYN61WzxKiBDXE"


# # Creating an function to be used in other pyrhon files
# def return_dataframe(): 
#     input_variables = {
#         "Accept" : "application/json",
#         "Content-Type" : "application/json",
#         "Authorization" : "Bearer {token}".format(token=TOKEN)
#     }
     
#     today = datetime.datetime.now()
#     yesterday = today - datetime.timedelta(days=2)
#     yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
#     playlist_id = playlist_url.split("/")[-1]
#     playlist_tracks_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    
#     r = requests.get(playlist_tracks_url, headers=input_variables)

#     if r.status_code != 200:
#         print("Failed to retrieve data from Spotify API.")
#         return None

#     data = r.json()
#     song_names = []
#     artist_names = []

#     for track in data["items"]:
#         song_names.append(track["track"]["name"])
#         artist_names.append(track["track"]["artists"][0]["name"])

#     song_dict = {
#         "song_name": song_names,
#         "artist_name": artist_names
#     }

#     song_df = pd.DataFrame(song_dict, columns=["song_name", "artist_name"])
#     return song_df

# playlist_url = "https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n"
# df = return_dataframe(playlist_url)
# if df is not None:
#     print(df)










    # Download all songs you've listened to "after yesterday", which means in the last 24 hours      
    # r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = input_variables)
    # ## https://api.spotify.com/v1/playlists/{playlist_id}/tracks
    # # playlist_tracks_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/track
    # data = r.json()
    # song_names = []
    # artist_names = []
    # played_at_list = []
    # timestamps = []

    # # Extracting only the relevant bits of data from the json object      
    # for song in data["items"]:
    #     song_names.append(song["track"]["name"])
    #     artist_names.append(song["track"]["album"]["artists"][0]["name"])
    #     played_at_list.append(song["played_at"])
    #     timestamps.append(song["played_at"][0:10])
        
    # # Prepare a dictionary in order to turn it into a pandas dataframe below       
    # song_dict = {
    #     "song_name" : song_names,
    #     "artist_name": artist_names,
    #     "played_at" : played_at_list,
    #     "timestamp" : timestamps
    # }
    # song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"])
    # return song_df




   