import requests
from django.shortcuts import render

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbchfhchf031305002'

# Create your views here.
def Attention_books(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '5',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
        'Cover': 'Big'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
            'description': item['description'],
            'cover': item['cover'], #오타였음
        }
        result.append(info)
    print(result)
    context = {
        'result': result
    }

    return render(request, 'recommend/Attention_books.html', context)

def Bestseller_books(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': '5',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
        'Cover': 'Big'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
            'description': item['description'],
            'cover': item['cover'], #오타였음
        }
        result.append(info)
    print(result)
    context = {
        'result': result
    }

    return render(request, 'recommend/Bestseller_books.html', context)

def Editor_books(request):

    return render(request, 'recommend/Editor_books.html')

def Vlogger_books(request):

    params = {
        'ttbkey': API_KEY,
        'QueryType': 'BlogBest',
        'MaxResults': '5',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
        'Cover': 'Big'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
            'description': item['description'],
            'cover': item['cover'], #오타였음
        }
        result.append(info)
    print(result)
    context = {
        'result': result
    }

    return render(request, 'recommend/Vlogger_books.html', context)

def main(request):
    return render(request, 'base.html')