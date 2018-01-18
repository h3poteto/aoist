from django.shortcuts import render

from front.models.picture import Picture

def index(request):
    pictures = Picture.objects.all()
    context = {
        'pictures': pictures,
    }
    return render (request, 'front/pictures/index.html', context)

