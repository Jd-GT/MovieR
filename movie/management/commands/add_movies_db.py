from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Load movies from movie_descriptions.json into the Movie model'

    def handle(selt, *args, **kwargs):


        json_file_path = 'movie/management/commands/movies.json'
#Load dala from the JSON file
        with open(json_file_path, 'r') as file:
            movies = json.load(file)
#Add products to the database
        for i in range(100):
            movie =movies[i]
            exist= Movie.objects.filter(title = movie['title']).first() #Se asegura que la película no exista en la b
            if not exist:
                Movie.objects.create(title = movie['title'],
                                image ='movie/images/Barbie.png', genre= movie['genre'],
                                year =movie['year'])
