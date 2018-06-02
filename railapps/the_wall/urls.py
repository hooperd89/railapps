from django.urls import path
from . import views

app_name ='the_wall'


urlpatterns = [
    path('',views.IndexView.as_view(),name='wall-index'),
    path('overview/work',views.WorkListView.as_view(),name='work_list'),
    path('overview/<int:pk>/',views.WorkDetailView.as_view(),name='work_detail'),
    path('overview/create',views.WorkCreateView.as_view(),name='work_create'),
    path('overview/<int:pk>/update',views.WorkUpdateView.as_view(),name='work_update'),
    path('overview/<int:pk>/delete',views.WorkDeleteView.as_view(),name='work_delete'),

]
