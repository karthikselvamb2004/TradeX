from django.urls import path
from .import views

urlpatterns = [
    path('index', views.index,name='index'),
    path('adminhome', views.adminhome,name='adminhome'),
    path('userindex', views.userindex,name='userindex'),
    path('', views.regis,name='signup'),
    path('table', views.tablecontent,name='table'),
    path('signin', views.loginform,name='signin'),
    path('userprofile', views.userprofile,name='userprofile'),
    path('datatable', views.datatable,name='datatable'),
    path('news_list', views.news_list, name='news_list'),
    path('add', views.add_news, name='add_news'),
    path('delete/<int:news_id>/', views.delete_news, name='delete_news'),
    path('edit/<int:news_id>/', views.edit_news, name='edit_news'),
    path('news', views.user_news_view, name='user_news'),
    path('approve_user/<int:id>/', views.approve_user, name='approve_user'),
    path('unapprove_user/<int:id>/', views.unapprove_user, name='unapprove_user'),
    path('profile', views.profile,name='profile'),
    path('community', views.community,name='community'),
    path('chat', views.chat,name='chat'),
]
    



