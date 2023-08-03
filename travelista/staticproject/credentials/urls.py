

from django.urls import path
from .  import views

urlpatterns = [
    
        path('registration',views.regfun,name='regfun'),
        path('login',views.logfun,name='logfun'),
        path('logout',views.logoutfun,name='logoutfun'),
]