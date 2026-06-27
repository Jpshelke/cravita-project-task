from django.urls import path
from ....mysite.myfirstproject import views

urlpatterns = [

    path("", views.home, name="home"),

    path("login/", views.login_page, name="login"),

    path("dashboard/", views.dashboard, name="dashboard"),

]