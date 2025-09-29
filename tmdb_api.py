import requests
import os
from dotenv import load_dotenv

#Loads variables stored in dotenv
load_dotenv()

ACCESS_TOKEN = os.getenv('TMDB_ACCESS_TOKEN')

base_url = 'https://api.themoviedb.org/3/discover/movie'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'accept': 'application/json'
}
 
params = {
    'include_adult': 'false', 
    'include_video': 'false',
    'language': 'en-US',
    'page': 1,
    'sort_by': 'popularity'
}

def get_request(params, headers):
    try:
        response = requests.get(url=base_url, params=params, headers=headers)
        if response == 200:
            return response.json()
    except requests.exceptions.RequestException:
        return
    
def get_now_playing_movies():
    endpoint = f'{base_url}/now_playing'
    pass

def get_popular_movies():
    endpoint = f'{base_url}/popular'
    pass

def get_top_movies():
    endpoint = f'{base_url}/top_rated'
    pass

def get_upcoming_movies():
    endpoint = f'{base_url}/upcoming'
    pass