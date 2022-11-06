from django.urls import path, include
from dbproject.views.index import index

urlpatterns = [
    path("", index, name="index"),

]