from django.urls import path
from . import views

app_name ='the_wall'


urlpatterns = [
    path('',views.IndexView.as_view(),name='wall-index'),
    path('work/',views.WorkListView.as_view(),name='work_list'),
    path('work/<int:pk>/',views.WorkDetailView.as_view(),name='work_detail'),
    path('work/create',views.WorkCreateView.as_view(),name='work_create'),
    path('work/<int:pk>/update',views.WorkUpdateView.as_view(),name='work_update'),
    path('work/<int:pk>/delete',views.WorkDeleteView.as_view(),name='work_delete'),

    path('occupation/',views.OccupationListView.as_view(),name='occupation_list'),
    path('occupation/<int:pk>/',views.OccupationDetailView.as_view(),name='occupation_detail'),
    path('occupation/create',views.OccupationCreateView.as_view(),name='occupation_create'),
    path('occupation/<int:pk>/update',views.OccupationUpdateView.as_view(),name='occupation_update'),
    path('occupation/<int:pk>/delete',views.OccupationDeleteView.as_view(),name='occupation_delete'),

]
