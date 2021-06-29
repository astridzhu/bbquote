# bbquote/lib.py
import requests


def get_quote():
    url = 'https://movie-quote-api.herokuapp.com/v1/quote/'  # alternative API
    # url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
    response = requests.get(url).json()

    return f"{response['quote']}    - {response['role']}"


if __name__ == "__main__":
    print(get_quote())
