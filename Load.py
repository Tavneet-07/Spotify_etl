import Extract
import Transform
import sqlalchemy 
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3
from sqlalchemy import create_engine

DATABASE_LOCATION = "postgresql://spotify:12345@localhost:5432/spotify123"
file_path='Transform.py'

if __name__ == "__main__":


#Importing the songs_df from the Extract.py
    load_df=Extract.return_dataframe(playlist_url="https://api.spotify.com/v1/artists/6eUKZXaKkcviH0Ku9w2n3V/top-tracks?country=US")
    if(Transform.Data_Quality(load_df) == False):
        raise ("Failed at Data Validation")
    Transformed_df=Transform.Transform_df(load_df)
    #The Two Data Frame that need to be Loaded in to the DataBase

#Loading into Database
    engine = create_engine(DATABASE_LOCATION)
   # conn = sqlite3.connect('my_played_tracks.sqlite')
    #cursor = conn.cursor()
    # with open(file_path,'r') as file:
    #     for line in file:
    #         song_value,artist_value=line.strip().split(',')
    #         sql_query = f"INSERT INTO my_played_tracks (song_name, artist_name) VALUES ('{song_value}', '{artist_value}');"
    #         print(sql_query)

    #SQL Query to Create Played Songs
    sql_query_1 = """
        CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200)
)
        """
    sql_query_2= """
INSERT INTO my_played_tracks (song_name, artist_name)
VALUES ('I Don't Care', 'Ed Sheeran');

"""
    #SQL Query to Create Most Listened Artist
    # sql_query_2 = """
    # CREATE TABLE IF NOT EXISTS fav_artist(
        
    #     artist_name VARCHAR(200),
    #     count VARCHAR(200)
        
    # )
    # """
    #cursor.execute(sql_query_1)
    # cursor.execute(sql_query_2)
   # print("Opened database successfully")

    # with open(file_path, 'r') as file:
    #     for line in file:
    #         song_value, artist_value = line.strip().split(',')
    #         # Construct and execute SQL INSERT query
    #         insert_query = f"INSERT INTO my_played_tracks (song_name, artist_name) VALUES ('{song_value}', '{artist_value}')"
    #         with engine.connect() as connection:
    #             connection.execute(insert_query)
    #             print(f"Inserted: {song_value}, {artist_value}")



     # Insert data into the database
    # for index, row in Transformed_df.iterrows():
    #     song_value = row['song_name']
    #     artist_value = row['artist_name']
    #     insert_query = f"INSERT INTO my_played_tracks (song_name, artist_name) VALUES ('{song_value}', '{artist_value}')"
    #     with engine.connect() as connection:
    #         connection.execute(insert_query)
    #         print(f"Inserted: {song_value}, {artist_value}")

    #We need to only Append New Data to avoid duplicates
    with engine.connect() as connection:
        connection.execute(sql_query_1)
        connection.execute(sql_query_2)
        print("opened database succesfully")
    try:
        load_df("my_played_tracks", engine, index=False, if_exists='append')
    except:
        print("Data already exists in the database")
    # try:
    #     Transformed_df.to_sql("fav_artist", engine, index=False, if_exists='append')
    # except:
    #     print("Data already exists in the database2")

    #cursor.execute('DROP TABLE my_played_tracks')
    #cursor.execute('DROP TABLE fav_artist')

    #conn.close()
    print("Close database successfully")
    
    