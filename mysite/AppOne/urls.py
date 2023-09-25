from django.urls import path
from AppOne import views

app_name = 'AppOne'

urlpatterns = [
    path('AppOne/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    
]
