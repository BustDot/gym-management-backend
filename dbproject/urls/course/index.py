from django.urls import path
from dbproject.views.course.list_courses import ListCoursesView
from dbproject.views.coach.coach import CoachView

urlpatterns = [
    path('', ListCoursesView.as_view(), name='list_coaches'),
    # path('<p1>/', CoachView.as_view(), name='coach'),

]