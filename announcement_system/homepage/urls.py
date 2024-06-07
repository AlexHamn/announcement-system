from django.urls import path
from . import views
from tts import views as tts_views

urlpatterns = [
    path('', views.index, name='index'),
    path('subcategory/<int:category_id>/', views.subcategory, name='subcategory'),
    path('announcement/<int:subcategory_id>/', views.announcement, name='announcement'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('generate-audio/', tts_views.generate_announcement_audio, name='generate_audio'),
]