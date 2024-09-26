import requests
from django.shortcuts import render, redirect
from . models import Report
from . forms import ReportForm

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbchfhchf031305002'

# API 관련 함수들
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


# 독후감 관련 함수 모임

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


def create(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save()
            return redirect('recommend:detail', report.pk)
    form = ReportForm()
    context = {
        'form':form
    }
    return render(request, 'report_book/new.html', context)


def delete(request,pk):
    pk_report = Report.objects.get(pk = pk)
    pk_report.delete()
    return redirect('recommend:book_report')


def update(request, pk):
    pk_report = Report.objects.get(pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST, instance=pk_report)
        if form.is_valid():
            form.save()
            return redirect('recommend:detail', pk_report.pk)
        
    form = ReportForm(instance=pk_report)
    context = {
        'form' : form,
        'report': pk_report,
    }
    return render(request, 'report_book/update.html', context)

############################################################

def main(request):
    return render(request, 'base.html')