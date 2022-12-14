from django.urls import path
from dbproject.views.sysuser.list_sysusers import ListSysUsersView

urlpatterns = [
    path('list/', ListSysUsersView.as_view(), name='list_sysusers'),
]