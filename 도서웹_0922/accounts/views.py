from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .models import Article



# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('recommend:book_report')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('recommend:book_report')


def signup(request):
    if request.user.is_authenticated:
        return redirect('recommend:book_report')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recommend:book_report')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    # 누가 요청한건지 User모델에서 검색할 필요가 없다.
    # request 객체에 요청을 보내는 user 정보가 함께 들어있기 때문.
    request.user.delete()
    return redirect('recommend:book_report')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('recommend:book_report')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:update')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


@login_required
def my(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/my.html', context)


@login_required
def follow(request, pk):
    User = get_user_model()
    person = User.objects.get(pk=pk)
    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:my', person.username)


####웹 크롤링####
def get_google_data(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    # Chrome 옵션 설정
    options = Options()
    options.add_argument('--headless')  # 브라우저를 숨기고 백그라운드에서 실행

    # 크롬 브라우저가 열린다. 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source 
    soup = BeautifulSoup(html, "html.parser")

    # div 태그 중 g 클래스를 가진 모든 요소 선택
    # 개발자 도구로 어떤 클래스를 가져올지 보고 정하면 된다.
    g_list = soup.select("div.g")
    results = []

    # 해당 요소를 반복하며
    for g in g_list:
        title_elem = g.select_one(".LC20lb.MBeuO.DKV0Md")
        link_elem = g.select_one("a")
        
        if title_elem and link_elem:
            title = title_elem.text
            link = link_elem.get('href')
            if link.startswith('/url?q='):
                link = link.split('/url?q=')[1].split('&')[0]
            results.append({'title': title, 'link': link})
    
    return results


def search(request):
    #사용자가 검색을 하면 크롤링을 진행
    if request.method == 'POST':
        query = request.POST.get('query')
        results = get_google_data(query)
        
        for result in results:
            # #아티글에 저장할건데 중복 없이 저장.
            # Article.objects.create(query= query, title = title)
            # if Article.objects.filter(query = query, title = title).exists():
            #     Article.objects.create(query= query, title = title)

            #있으면 가져오고 없으면 저장해라.
            Article.objects.get_or_create(
                query=query,
                title=result['title'],
                link=result['link']
            )

        context = {
            # 'results': Article.objects.all()
            'query':query,
            'results': Article.objects.filter(query=query)
        }

        #아니라면, 그냥 검색 페이지 제공
        return render(request, 'accounts/search.html', context)
    
    return render(request, 'accounts/search.html')
####