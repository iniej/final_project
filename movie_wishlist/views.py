from django.shortcuts import render, redirect
from .forms import RegistrationForm, WatchedListForm, WatchListForm, PopularMoviesForm
from django.contrib.auth import authenticate, login, logout
import requests
from movie_wishlist import movie_data
from .models import WatchList
# Create your views here.

def homepage(request):
    return render(request, 'movie_wishlist/homepage.html')

def popularMovies(request):
    form = PopularMoviesForm()
    search_movie = request.GET.get('search_movie')
    return render(request, 'movie_wishlist/popular_movies.html', {'form': form})


def my_profile(request):
    return render(request, 'movie_wishlist/my_profile.html')


def user(request):
    return render(request, 'movie_wishlist/user.html')

def watch_list(request):
    watchlist = WatchList.objects.all()
    form = WatchListForm()
    search_movie = request.GET.get('search_movie')
    args = {'form' : form, 'watchlist': watchlist}
    return render(request, 'movie_wishlist/watchlist.html', args)
    # return render(request, 'movie_wishlist/watchlist.html', {'form' : form, 'wishlist': wishlist})

def movie_list(request):

    title = request.GET.get('search_movie')
    movie = movie_data.movie_api(title)
    # title = request.GET.get('search_movie')
    # movie = movie_data.movie_api(title)

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
    title = request.POST.get("Title")
    year = request.POST.get('Year')
    actor = request.POST.get('Actors')
    director = request.POST.get('Director')

    new_movie = WatchList(name = title, actor = actor, director = director, year = year)
    if not 'Cancel' in request.POST:
        new_movie.save()

    return render(request, 'movie_wishlist/user.html')
