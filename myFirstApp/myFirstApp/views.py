from django.shortcuts import render
import requests


def home(request):
    return render(request, 'pages/home.html')


def product(request):
    response = requests.get(
        'https://jsonplaceholder.typicode.com/posts/1/comments').json()
    return render(request, 'pages/product_list.html', {'response': response})
