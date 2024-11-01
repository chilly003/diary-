import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from . models import Report, Comment
from . forms import ReportForm, CommentForm

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
    comment_form = CommentForm()
    comments = pk_report.comment_set.all()

    context = {
        'report' : pk_report,
        'comment_form' : comment_form,
        'comments': comments
    }
    return render(request, 'report_book/detail.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('recommend:detail', report.pk)
    form = ReportForm()
    context = {
        'form':form
    }
    return render(request, 'report_book/new.html', context)


@login_required
@require_POST
def delete(request,pk):
    report = get_object_or_404(Report, pk = pk)
    if request.user == report.user:
        report.delete()
        return JsonResponse({'ci_delete':True})
    return JsonResponse({'ci_delete':False})
    

@login_required
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

@login_required
def comments_create(request, pk):
    report = Report.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.report = report
        comment.user = request.user
        comment.save()
        return redirect('recommend:detail', report.pk)
    context = {
        'report' : report,
        'comment_form': comment_form,
    }
    return render(request, 'report_book/detail.html', context)

@login_required
def comments_delete(request, article_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})