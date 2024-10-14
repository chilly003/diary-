from django.urls import path
from . import views

app_name = 'recommend'

urlpatterns = [
    path('Attention_books/', views.Attention_books, name= 'Attention_books'),
    path('Bestseller_books/', views.Bestseller_books, name= 'Bestseller_books'),
    path('My_book/', views.My_book, name= 'My_book'),
    path('Vlogger_books/', views.Vlogger_books, name= 'Vlogger_books'),
    path('book_report/', views.Book_report, name= 'book_report'),
    path('<int:pk>/', views.detail, name= 'detail'),
    # path('new/', views.new, name= 'new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path(
        '<int:article_pk>/comments/<int:comment_pk>/delete/',
        views.comments_delete,
        name='comments_delete',
    ),

]

