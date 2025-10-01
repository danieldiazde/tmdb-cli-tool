from tmdb_api import fetch_data

def format_response(response: dict) -> str:
    results = response.get('results', [])
    if not results:
        return 'No movies found'
    output = []

    for index, movie in enumerate(results,1):
        movie_title = movie.get('title', 'N/A')
        overview = movie.get('overview', 'No overview available')
        release_date = movie.get('release_date', 'Unknown')

        cut_overview = overview[:200] + '...' if len(overview)>200 else overview
        line = f'\n{index}. 🎬 "{movie_title}" ({release_date}):\n   {cut_overview}\n'
        output.append(line)
    return ''.join(output)

        