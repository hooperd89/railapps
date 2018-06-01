from django.urls import path
from . import views

app_name ='the_wall'


urlpatterns = [
    path('',views.IndexView.as_view(),name='wall-index'),
    path('overview/',views.WorkListView.as_view(),name='work_list'),
    path('overview/<int:pk>',views.WorkDetailView.as_view(),name='work_detail'),
]
