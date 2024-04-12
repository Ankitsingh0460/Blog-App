
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.Login,name = "login"),
    path('signup',views.Signup,name = "Signup"),
    path('',views.Home,name = "home"),
    path('features',views.Features,name = "features"),
    path('myblogs',views.Myblogs,name = "myblogs"),
    path('aboutus',views.Aboutus,name = "aboutus"),
    path('delete/<int:id>',views.Delete,name = "delete"),
    path('update/<int:id>',views.Update,name = "update"),
    path('myblogs2',views.Myblogs2,name = "myblogs2"),
    path('features2',views.Features2,name = "features2"),
    path('home2',views.Home2,name = "home2"),
    path('aboutus2',views.Aboutus2,name = "aboutus2"),
]

