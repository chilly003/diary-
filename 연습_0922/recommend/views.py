import requests
from django.shortcuts import render, redirect
from . models import Report

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

def My_book(request):
    return render(request, 'recommend/my_book.html')

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

############################################################
###########독후감 관련 함수 모임############################

def Book_report(request):
    all_report = Report.objects.all()
    context = {
        'report_all' : all_report
    }
    return render(request, 'report_book/book_report.html', context)


def detail(request, pk):
    pk_report = Report.objects.get(pk = pk)
    context = {
        'report' : pk_report
    }
    return render(request, 'report_book/detail.html', context)


def new(request):
    return render(request, 'report_book/new.html')

def create(request):
    name = request.POST.get('name')
    author = request.POST.get('author')
    report = request.POST.get('report')
    make_report = Report(name=name,author=author,report=report)
    make_report.save()
    return redirect('recommend:book_report')

def delete(request,pk):
    pk_report = Report.objects.get(pk = pk)
    pk_report.delete()
    return redirect('recommend:book_report')

############################################################



def main(request):
    return render(request, 'base.html')