from django.shortcuts import render
from .models import Movie

# Create your views here.
def home(request):

    searchTerm =request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies= Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})
    # return render(request, 'home.html',{'name':'El Gran david'})

def about(request):
    return render(request, 'about.html')
    
def abou(request):
    return render(request, 'abou.html')