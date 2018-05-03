import requests
import os



#
# if 'search_movie' in request.GET:
#     title = request.GET.get('search_movie')
def movie_api(name):
    apikey = '6d42cd22'
    url = 'http://www.omdbapi.com/?apikey='+apikey+'&'+'t='+name
    movie = {}
    response = requests.get(url)
    movie1 = response.json()
    keys = ['Title', 'Year', 'Actors', 'Director']
    for key in keys:
        movie.update({key: movie1[key]})

    return movie
# def get_movie_info(name):
#     apikey = '6d42cd22'
# '
#     movie_info = {}
#     url = 'http://www.omdbapi.com/?apikey='+apikey+'&'+'t='+name
#     response = requests.get(url)
#     movie = response.json()
#     keys = ['Title', 'Year', 'Actors', 'Director']
#     for key in keys:
#         movie_info.update({key: movie[key]})
#     return movie_info
