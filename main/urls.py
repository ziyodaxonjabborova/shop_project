from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path("",home,name="home"),
    path("create/",create,name="create"),
    path("detail/<int:pk>/",detail,name="detail"),
    path("update/<int:pk>/",update,name="update"),
    path("delete/<int:pk>/",delete,name="delete")
]