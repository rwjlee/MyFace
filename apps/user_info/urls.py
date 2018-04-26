from django.urls import path
from . import views

app_name = 'user_info'

urlpatterns = [
    path('', views.index, name ='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
    path('search_results/<str:term>', views.search_results, name='search_results'),
    path('following_page', views.following_page, name='following_page'),
]