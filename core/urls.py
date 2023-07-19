
from core import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('test/<int:pk>', views.Test.as_view(), name='test'),
]
