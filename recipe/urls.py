"""
URL configuration for trial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from recipe import views
admin.site.site_header = "recipe-bot Admin"
admin.site.site_title = "recipe-bot Admin Portal"
admin.site.index_title = "Welcome to recipe-bot Portal"
urlpatterns = [
    path("",views.index, name="home"),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path("about",views.about, name="about"),
    path("contact",views.contact,name="contact" ),
    path("recipe_on_mood",views.mood,name="mood" ),
    path("recipe_on_dish_name",views.dishname,name="dishname" ),
    path("recipe_on_ingredients",views.ingredients,name="ingredients" ),
    path('signup',views.SignupPage,name='signup'),
    path('login',views.LoginPage,name='login'),
    path('logout',views.LogoutPage,name='logout'),
]
