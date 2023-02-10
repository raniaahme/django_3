"""mylib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from catagory import views
from book import views as bookviews
from account import views as accountview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.List,name='Catagory_List'),
    path('Book/Add',bookviews.Add,name='Book_Add'),
    path('booklist',bookviews.List,name='Book_List'),
    path('Login',accountview.mylogin,name='Login'),
    path('Logout',accountview.mylogout,name='Logout'),
    path('Register',accountview.myregister,name='Register'),
    path('Catatory/Add', views.Add, name='Catagory_Add'),
    path('Catatory/Update/<int:catid>', views.Update, name='Catagory_Update'),
    path('Login2',accountview.Loginview.as_view(),name='Login2'),
    path('Logout2',accountview.mylogout2,name='Logout2'),
    path('Register2',accountview.myregister2,name='Register2'),
    path('List',accountview.List.as_view(),name='Account_List'),
]
