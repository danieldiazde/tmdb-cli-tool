from tmdb_api import fetch_data

def format_response(response: dict) -> str:
    results = response.get('results', None)
    if results:
        counter = 1
        for movie in results:
            movie_title = movie.get('title')
            overview = movie.get('overview')
            release_date = movie.get('release_date')
            print(f'\n{counter}. "{movie_title}" ({release_date}):{overview[:200]}...\n')
            counter+=1