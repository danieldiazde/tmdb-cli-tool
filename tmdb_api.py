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

specifications = {'playing', 'popular', 'top', 'upcoming'}
    
def fetch_data(specification):
    if not ACCESS_TOKEN:
        print('Error: TMDB ACCESS TOKEN not found, please check your .env file')
        return None
    if specification not in specifications:
        return None
    if specification == 'playing':
        path = '/now_playing'
    elif specification == 'popular':
        path = '/popular'
    elif specification == 'top':
        path = '/top_rated'
    elif specification == 'upcoming':
        path = '/upcoming'

    endpoint = base_url+path

    try:
        response = requests.get(url=endpoint, params=params, headers= headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'An error ocurred: {e}')
    return None
