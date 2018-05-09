## MOVIE_MANGER App

This application let user make a movie to watch list (watchlist). When the user enters the movie's
the application makes an api call to OMDB and get the movie and put it into a watchlist table. A movie can be moved to a watched list, after the movie has been watched.

### To install App

1. Create and activate a virtual environment. Use Python3 as the interpreter.

2. Navigate to the movie_manager directory

3. pip install -r requirements.txt

4. python manage.py makemigrations

5. python manage.py migrate

6. python manage.py runserver

Site at

127.0.0.1:8000

Need a free OMDB API KEY 

* Movie Trailer api call from Youtube is not working yet.
* Rating functionality is not working yet
