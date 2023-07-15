
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homefun,name="homefun"),
    path('delete/<int:taskid>/',views.deletefun,name="deletefun"),
    path('update/<int:id>/',views.updatefun,name='updatefun'),
    path('cbview/',views.Tasklistview.as_view(),name='cbview'),
    path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete'),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate'),
]
