import argparse

parser = argparse.ArgumentParser(description='Parser the movies you want to watch')
parser.add_argument('--type', type=str, help='Type of information you want')


def main():
    args = parser.parse_args()
    pass
