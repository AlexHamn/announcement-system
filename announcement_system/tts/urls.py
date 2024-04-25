from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_announcement_audio, name='generate_audio'),
    path('test/', views.test_view, name='test'),
]