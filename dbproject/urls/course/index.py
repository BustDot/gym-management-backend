from django.urls import path
from dbproject.views.course.list_courses import ListCoursesView
from dbproject.views.course.course import CourseView

urlpatterns = [
    path('', ListCoursesView.as_view(), name='list_coaches'),
    path('<p1>/', CourseView.as_view(), name='course'),

]