from django.shortcuts import render, redirect, get_object_or_404
from .forms import  WatchedListForm, WatchListForm, PopularMoviesForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
import requests
from movie_wishlist import movie_data
from .models import WatchList, WatchedList
from django.http.response import HttpResponseForbidden
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

def movie_list(request):
    title = request.GET.get('search_movie')
    movie = movie_data.movie_api(title)
    return render(request, 'movie_wishlist/movie.html',{'movie': movie})

def watched_list(request):
    watched_movie = WatchedList.objects.all()
    form = WatchedListForm()
    search_movie = request.GET.get('search_movie')
    return render(request, 'movie_wishlist/watchedlist.html', {'form': form, 'watched_movie' : watched_movie})


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
    movie_name = WatchList.objects.filter(name__iexact = title).all()
    # if not 'Cancel' in request.POST:
    if movie_name:
        message = 'That movie already exist in your database'
        return render(request, 'movie_wishlist/watchlist.html', {'message': message})
    else:
        new_movie.save()

    return render(request, 'movie_wishlist/user.html')


def add_to_watchedlist(request):
    title = request.POST.get("Name")
    year = request.POST.get('Year')
    director = request.POST.get('Director')
    actor = request.POST.get('Actors')
    watched_movie = WatchedList(name = title, actor= actor, director = director, year = year)
    if not 'Cancel' in request.POST:
        watched_movie.save()
        movie = WatchList.objects.filter(name__iexact = title)
        movie.delete()
    return render(request, 'movie_wishlist/user.html')


def movie_detail(request, pk):
    movie_detail = get_object_or_404(WatchList, pk = pk)
    return render(request, 'movie_wishlist/movie_detail.html', {'movie_detail': movie_detail})
