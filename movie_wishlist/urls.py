from django.conf.urls import url
from . import views
<<<<<<< HEAD

urlpatterns = [
    url(r'^$', views.homepage, name = 'homepage'),
    url(r'^popularmovies/$', views.popularMovies, name = 'popular_movies'),

    url(r'^myprofile/$', views.my_profile, name = 'my_profile'),
    url(r'^user/$', views.user, name = 'user'),
    url(r'^user/movies/watchlist/$', views.watch_list, name = 'watch_list'),
    url(r'^user/movies/watchedlist/$', views.watched_list, name = 'watched_list'),
    url(r'^user/movies/movielist/$', views.movie_list, name = 'movie_list'),
    url(r'^user/movies/movie_to_watch/$', views.add_to_watchlist, name = 'add_to_watchlist'),
=======
from django.contrib.auth import views as auth_views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import authenticate, login, logout


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^popular movies/$',views.popular_movies, name='popular_movies'),

    # User profile urls

    url(r'^user/profile/(?P<user_pk>\d+)/$', views.user_profile, name='user_profile'),
    
    url(r'^user/$', views.user_page, name = 'user_page'),
    url(r'^watch_list/$', views.watch_list, name = 'watch_list'),
    url(r'^watched_list/$', views.watched_list, name = 'watched_list'),


>>>>>>> 3e978d94bd540b321e23aae828bae26654f88ae8
]
