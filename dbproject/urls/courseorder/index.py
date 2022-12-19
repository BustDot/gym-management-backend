from django.urls import path
from dbproject.views.courseorder.course_order import CourseOrderView
from dbproject.views.courseorder.list_user_order import ListUserOrderView

urlpatterns = [
    path('list/<p1>/', ListUserOrderView.as_view(), name='list_user_order'),
    path('<p1>/', CourseOrderView.as_view(), name='course_order'),

]