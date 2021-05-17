import requests

def get_quote():

    url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
    return requests.get(url).json()[0]
