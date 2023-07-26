
from django.urls import include, path
from . import views

app_name='movieapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detailfun,name='detailfun'),
    path('add/',views.addfun,name="addfun"),
    path('update/<int:id>/',views.updatefun,name="updatefun"),
    path('delete/<int:id>/',views.deletefun,name="deletefun")
]
