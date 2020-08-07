from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie
from datetime import date
# 2 - extract a session
session = Session()



movies = session.query(Movie) \
    .filter(Movie.release_date > date(2015, 1, 1)) \
    .all()

print('\n### All movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')


