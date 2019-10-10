from django.shortcuts import render


def home(request, Params):

    return render(request, 'private/home.html', {'Params': Params})
