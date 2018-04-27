from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user_info'

urlpatterns = [
    path('', views.index, name ='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
    path('search_results/<str:term>', views.search_results, name='search_results'),
    path('following_page', views.following_page, name='following_page'),
    path('add_follow/<int:following_id>', views.add_follow, name = 'add_follow'),
    path('follower_page', views.follower_page, name='follower_page'),
    path('delete_follow/<int:follow_id>', views.delete_follow, name = 'delete_follow'),
    path('user_page/<int:user_id>', views.user_page, name='user_page'),
    path('add_post', views.add_post, name='add_post'),
    path('delete_post/<int:post_id>', views.delete_post, name = 'delete_post'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('photo_page/<int:user_id>', views.photo_page, name='photo_page'),
    path('add_photo', views.add_photo, name='add_photo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)