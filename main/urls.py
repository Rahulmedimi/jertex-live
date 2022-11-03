from django.urls import path
from . import views


urlpatterns=[
    path("",views.home,name='home'),
    path('feed',views.feed,name="feed"),
    path("/serviceproviderregister",views.serviceproviderregister,name="serviceproviderregister"),
    path('accounts/login',views.socialaccountsconsumer,name="socialaccountsconsumer"),
    path('login',views.loginuser ,name="login"),
    path('logout', views.logoutuser , name="logout"),
    path('registeroption' , views.registeroption,name="registeroption"),
    path('consumerregister',views.consumerregister,name="consumerregister"),
    path('userprofile',views.userprofile,name='userprofile'),
    path('orderservice',views.orderservice,name='orderservice'),
    path('serviceproviderinfo/<str:text>',views.serviceproviderinfo,name='serviceproviderinfo'),
    path('sucesspage',views.sucesspage,name="sucesspage"),
    path('serviceproviderpost/',views.serviceproviderpost,name='serviceproviderpost'),
]