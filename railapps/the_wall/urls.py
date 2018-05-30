from django.urls import path
from . import views
from the_wall.views import (OccupationListView)
app_name ='the_wall'
urlpatterns = [
    path('overview/', views.OccupationListView.as_view(), name='occupation_list'),
]
