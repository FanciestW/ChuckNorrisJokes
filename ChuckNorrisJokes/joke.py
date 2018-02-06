""" Chuck Norris Jokes Module """
import sys
import json
import requests

API_URL = 'https://api.chucknorris.io/jokes/'

def main():
    """ main function of program """
    print(get_joke_categories())
    # get_joke('dev')

def get_joke(joke_category):
    """ Get a Chuck Norris joke from a specific category """
    parameters = {
        "category" : joke_category
    }
    api_endpoint_string = API_URL + "random" + build_api_query(parameters)
    try:
        response = requests.get(api_endpoint_string)
        response_json = response.json()
        print(response_json['value'])
    except:
        print("Error", sys.exc_info()[0])
        raise

def build_api_query(query_parameters):
    query_string = '?'
    for key, value in query_parameters.items():
        query_string += key + '=' + value + '&'
    return query_string[:-1]

def get_joke_categories():
    """ Returns an array of joke categories """
    try:
        response = requests.get(API_URL + 'categories')
        response_json = response.json()
        return response_json
    except:
        print("Error", sys.exc_info()[0])
        raise
    

main()
