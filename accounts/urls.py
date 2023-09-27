from django.urls import path

from accounts import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.loginPage, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logOut, name="logout"),
]
