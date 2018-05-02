from django.shortcuts import render, redirect
from .forms import RegistrationForm, WatchedListForm, WatchListForm, PopularMoviesForm
from django.contrib.auth import authenticate, login, logout
import requests
from movie_wishlist import movie_data
from .models import WatchList
# Create your views here.



# Create your views here.
def homepage(request):
    return render(request, 'movie_wishlist/homepage.html')

def popularMovies(request):
    form = PopularMoviesForm()
    search_movie = request.GET.get('search_movie')
    return render(request, 'movie_wishlist/popular_movies.html', {'form': form})

# def login(request):
#     return render(request, 'movie_management_app/login.html')
#
# def logout(request):
#     return redirect(request, 'movie_management_app/homepage.html')

def my_profile(request):
    return render(request, 'movie_list/my_profile.html')

# def register(request):
#     return render(request, 'movie_management_app/register.html')

def user(request):
    return render(request, 'movie_wishlist/user.html')

def watch_list(request):
    form = WatchListForm()
    wishlist = WatchList.objects.all()
    search_movie = request.GET.get('search_movie')
    return render(request, 'movie_wishlist/watchlist.html', {'form' : form, 'wishlist': wishlist})

def movie_list(request):
    # apikey = '6d42cd22'
    # movie= {}
    # if 'search_movie' in request.GET:
    #     title = request.GET.get('search_movie')
    #     print(title)
    #     url = 'http://www.omdbapi.com/?apikey='+apikey+'&'+'t='+title
    #     response = requests.get(url)
    #     movie = response.json()['Title']
    # else:


    title = request.GET.get('search_movie')
    movie = movie_data.movie_api(title)

    return render(request, 'movie_wishlist/movie.html',{'movie': movie})

def watched_list(request):
    form = WatchedListForm()
    search_movie = request.GET.get('search_movie')
    return render(request, 'movie_wishlist/watchedlist.html', {'form': form})
def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return redirect('homepage')

        else :
            message = 'Please check the data you entered'
            return render(request, 'registration/register.html', { 'form' : form , 'message' : message } )


    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html', { 'form' : form } )

def add_to_watchlist(request):
    name = request.POST.get("Title")
    year = request.POST.get('Year')
    actor = request.POST.get('Actors')
    director = request.POST.get('Director')

    new_movie = WatchList(title = name, actor = actor, director = director, year = year)


    new_movie.save()
    return render(request, 'movie_wishlist/user.html')
