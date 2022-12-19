from django.urls import path
from dbproject.views.coach.list_coaches import ListCoachesView
from dbproject.views.coach.coach import CoachView

urlpatterns = [
    path('', ListCoachesView.as_view(), name='list_coaches'),
    path('<p1>/', CoachView.as_view(), name='coach'),

]