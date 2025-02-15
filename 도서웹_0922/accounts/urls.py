from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('search/', views.search, name='search'),
    path('my/<username>/', views.my, name='my'),
    path('<int:pk>/follow/', views.follow, name='follow'),
]
