from django.shortcuts import render

from movie.models.youtube import Youtube

def index(request):
    youtubes = Youtube.objects.all()
    context = {
        'youtubes': youtubes,
    }
    return render(request, 'movie/youtubes/index.html', context)
