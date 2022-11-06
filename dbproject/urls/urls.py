from django.urls import path
from dbproject.views.views import index

urlpatterns = [
    path("", index, name="index"),
]