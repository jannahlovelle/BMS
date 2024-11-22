

from django.urls import path
from bms_user_authentication import views


urlpatterns =[
    path('', views.user_login, name='login'),  # Set the login page as the landing page
    # path('home/', views.home_page, name='home_page'),
    path('home/', views.user_homepage, name='home_page'),
    path('logout/', views.user_logout, name='logout'),

    path('profile/', views.profile, name='profile'),
    path('password/', views.change_password, name='change_password'),


    # path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    # path('user_list/', views.user_list, name='user_list'),
]