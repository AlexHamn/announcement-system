from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subcategory/<int:category_id>/', views.subcategory, name='subcategory'),
    path('announcement/<int:subcategory_id>/', views.announcement, name='announcement'),
    path('confirmation/', views.confirmation, name='confirmation'),
]