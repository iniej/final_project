from django.conf.urls import url
from . import views
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


]
