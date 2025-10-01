import argparse
from display import format_response
from tmdb_api import fetch_data

movie_types = {'playing', 'popular', 'top', 'upcoming'}

parser = argparse.ArgumentParser(description='Fetch movie info from TMDB')
parser.add_argument('--type', type=str, help='Type of movies to fetch', required=True, choices=movie_types)


def main():
    args = parser.parse_args()
    movie_data = fetch_data(specification=args.type)
    if movie_data:
       print(format_response(movie_data))

if __name__ == '__main__':
    main()
