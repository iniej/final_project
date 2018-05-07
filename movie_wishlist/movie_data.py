import requests
import os


apikey = '6d42cd22'
# Make an api call to get the movie
def movie_api(name):

    url = 'http://www.omdbapi.com/?apikey='+apikey+'&'+'t='+name
    movie = {}
    response = requests.get(url)
    movie1 = response.json()
    keys = ['Title', 'Year', 'Actors', 'Director']
    for key in keys:
        movie.update({key: movie1[key]})
    return movie
