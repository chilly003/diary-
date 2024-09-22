from django.urls import path
from . import views

app_name = 'recommend'

urlpatterns = [
    path('Attention_books', views.Attention_books, name= 'Attention_books'),
    path('Bestseller_books', views.Bestseller_books, name= 'Bestseller_books'),
    path('Editor_books', views.Editor_books, name= 'Editor_books'),
    path('Vlogger_books', views.Vlogger_books, name= 'Vlogger_books'),
]

