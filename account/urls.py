from django.urls import path
from .import views

urlpatterns=[
    
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('welcome/',views.welcome, name="welcome"),
    path('logout/',views.signout,name="signout"),
    path('view/',views.index,name="index"),
    path('welcome/add/',views.add,name="add"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('update/<int:id>/', views.update, name="update")

    

]