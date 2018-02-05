import requests
import json

def main():
    url = 'https://api.chucknorris.io/jokes/random'
    resJSON = requests.get(url).json()
    
    print(resJSON)

main()