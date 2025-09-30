import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

#Loads variables stored in dotenv
load_dotenv()

ACCESS_TOKEN = os.getenv('TMDB_ACCESS_TOKEN')

base_url = 'https://api.themoviedb.org/3/movie'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'accept': 'application/json'
}

params = {
    'include_adult': 'false', 
    'include_video': 'false', 
    'language': 'en-US',
    'page': '1'
}
    
def get_now_playing_movies():
    if not ACCESS_TOKEN:
        print('Error: TMDB ACCESS TOKEN not found, please check your .env file')
        return None
    endpoint = f'{base_url}/now_playing'

    try:
        response = requests.get(url=endpoint, params=params, headers= headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'An error ocurred: {e}')
    return None


print(get_now_playing_movies())



def get_popular_movies():
    endpoint = f'{base_url}/popular'
    pass

def get_top_movies():
    endpoint = f'{base_url}/top_rated'
    pass

def get_upcoming_movies():
    endpoint = f'{base_url}/upcoming'
    pass