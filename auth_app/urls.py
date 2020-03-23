from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
from .views import IndexView, profile, add, remove



# from . import views 

urlpatterns = [
    # path('signup/', views.signup, name="signup"),
    # path('login/', views.login, name="login"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cart/add/<int:id>', add, name='add'),
    path('cart/remove/<int:id>', add, name='remove')
]