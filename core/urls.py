
from core import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('view_attestation/', views.attestation_view, name='view_attestation'),

    path('home/<int:pk>/detail', views.DetailHome.as_view(), name='home_detail'),
    path('home/list', views.ListHome.as_view(), name='home_list'),
    path('home/<int:pk>/update', views.HomeUpdate.as_view(), name='home_update'),
    path('home/<int:pk>/delete', views.HomeDelete.as_view(), name='home_delete'),
    path('home/create', views.HomeCreate.as_view(), name='home_create'),
]
