from django.shortcuts import render
import random
# from django.http import HttpResponse


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    special = request.GET.get('special')
    numbers = request.GET.get('numbers')

    if special:
        characters.extend(list('@!#$%&?¡¿*+-_'))

    if uppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if numbers:
        characters.extend(list('1234567890'))

    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'password.html', {'password': generated_password})
