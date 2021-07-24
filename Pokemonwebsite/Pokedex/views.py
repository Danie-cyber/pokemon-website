from django.shortcuts import render
from django.http import HttpResponse
from .api import *
# Create your views here.


def home(request):
    return render(request, 'home.html', {'pokemon': 'Pikachu'})


def pokemon(request, pk_name):
    pk = Pokemon(pk_name)
    types = pk.types()
    moves = []
    ability = pk.ability()
    statistics = pk.stats()
    statistics = statistics.items()
    if(pk.len_moves() > 12):
        for i in range(12):
            moves.append(pk.moves(i))
    else:
        for i in range(pk.len_moves()):
            moves.append(pk.moves(i))
    temp = pk.game_version()
    if(temp > 0 and temp < 10):
        index = "00"+str(temp)
    elif(temp > 9 and temp < 100):
        index = "0"+str(temp)
    else:
        index = str(temp)

    return render(request, 'pokemon.html', {'name': pk.name.title(), 'types': types, 'moves': moves, 'index': index, 'ability': ability, 'statistics': statistics})
