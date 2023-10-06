import pylib.datasource as ds
from pprint import pprint
import pylib.templating as tp

movies = ds.get_movies()
pprint(movies)

pprint([movie[0] for movie in movies])
pprint([movie[0] for movie in movies if not movie[2]])
print(tp.TIME_REMAINING.format(*divmod(sum([duration for title, duration, viewed in movies if not viewed]), 60)))

