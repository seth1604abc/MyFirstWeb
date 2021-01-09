from django.shortcuts import render
from commodity.models import Music

def index(request):
    musics = Music.objects.all()
    context = {'musics': musics}
    return render(request, 'index.html', context=context)
