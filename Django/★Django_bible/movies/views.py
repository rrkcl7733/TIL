from django.shortcuts import redirect, render

from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()[::-1]
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

def create(request):
    movie = Movie()
    movie.title = request.GET.get('title')
    movie.audience = request.GET.get('audience')
    movie.release_date = request.GET.get('release_date')
    movie.genre = request.GET.get('genre')
    movie.score = request.GET.get('score')
    movie.poster_url = request.GET.get('poster_url')
    movie.description = request.GET.get('description')
    movie.save()
    return redirect('movies:index')

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
        'genres': ["코미디", "호러", "판타지"]
    }
    return render(request, 'movies/edit.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.title = request.GET.get('title')
    movie.audience = request.GET.get('audience')
    movie.release_date = request.GET.get('release_date')
    movie.genre = request.GET.get('genre')
    movie.score = request.GET.get('score')
    movie.poster_url = request.GET.get('poster_url')
    movie.description = request.GET.get('description')
    movie.save()
    return redirect('movies:detail', movie.pk)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')