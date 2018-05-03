from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name = 'homepage'),
    url(r'^popularmovies/$', views.popularMovies, name = 'popular_movies'),

    url(r'^myprofile/$', views.my_profile, name = 'my_profile'),
    url(r'^user/$', views.user, name = 'user'),
    url(r'^user/movies/watchlist/$', views.watch_list, name = 'watch_list'),
    url(r'^user/movies/watchedlist/$', views.watched_list, name = 'watched_list'),
    url(r'^user/movies/movielist/$', views.movie_list, name = 'movie_list'),
    url(r'^user/movies/movie_to_watch/$', views.add_to_watchlist, name = 'add_to_watchlist'),
]
