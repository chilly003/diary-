import requests
from django.shortcuts import render

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = ''

# Create your views here.
def Attention_books(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '10',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
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
            'cover': item['cover'], #이거 어케하지
        }
        result.append(info)
    print(result)
    context = {
        'result': result
    }

    return render(request, 'recommend/Attention_books.html', context)

def Bestseller_books(request):
    return render(request, 'recommend/Bestseller_books.html')

def Editor_books(request):
    return render(request, 'recommend/Editor_books.html')

def Vlogger_books(request):
    return render(request, 'recommend/Vlogger_books.html')

def main(request):
    return render(request, 'base.html')