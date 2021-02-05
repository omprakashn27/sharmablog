from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="/"),

    path('blogs/', views.blogs, name="blogs"),
    path('viewblog/<int:pk>', views.viewblog, name="viewblog"),

    path('addd-blog', views.addblog, name="addblog"),
    path('editblog/<int:pk>', views.editBlog, name="edit"),
    path('delete/<int:pk>', views.deleteBlog, name="delete"),

    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),
    
]