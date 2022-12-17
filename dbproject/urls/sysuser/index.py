from django.urls import path
from dbproject.views.sysuser.list_sysusers import ListSysUsersView
from dbproject.views.sysuser.sysuser import SysUserView

urlpatterns = [
    path('list/', ListSysUsersView.as_view(), name='list_sysusers'),
    path('<p1>/', SysUserView.as_view(), name='sysuser'),

]