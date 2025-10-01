import requests
import os
from dotenv import load_dotenv
from datetime import date, timedelta

today = date.today()

max_date_playing = (today+timedelta(weeks=1)).strftime('%Y-%m-%d')
min_date_playing = (today-timedelta(weeks=3)).strftime('%Y-%m-%d')

max_date_upcoming = (today+timedelta(weeks=5)).strftime('%Y-%m-%d')
min_date_upcoming = (today+timedelta(weeks=1)).strftime('%Y-%m-%d')

#Loads variables stored in dotenv
load_dotenv()
ACCESS_TOKEN = os.getenv('TMDB_ACCESS_TOKEN')

BASE_URL = 'https://api.themoviedb.org/3'

HEADERS = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'accept': 'application/json'
}

base_params = {
    'include_adult': 'false', 
    'include_video': 'false', 
    'language': 'en-US',
    'page': '1'
}

specifications = {'playing', 'popular', 'top', 'upcoming'}
    
def fetch_data(specification: str) -> dict:
    if not ACCESS_TOKEN:
        print('Error: TMDB ACCESS TOKEN not found, please check your .env file')
        return None
    if specification not in specifications:
        print(f'Specification {specification} is not valid')
        return None
    
    local_params = base_params.copy()

    if specification == 'playing':
        path = '/discover/movie'
        local_params['release_date.gte'] = min_date_playing
        local_params['release_date.lte'] = max_date_playing

    elif specification == 'popular':
        path = '/movie/popular'

    elif specification == 'top':
        path = '/movie/top_rated'

    elif specification == 'upcoming':
        local_params['release_date.gte'] = min_date_upcoming
        local_params['release_date.lte'] = max_date_upcoming
        path = '/discover/movie'

    endpoint = BASE_URL+path

    try:
        response = requests.get(url=endpoint, params=local_params, headers= HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'An error ocurred: {e}')
        return None
