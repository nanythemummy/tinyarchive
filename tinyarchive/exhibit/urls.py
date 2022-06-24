from django.urls import path
from . import views

urlpatterns = [
    path('', views.exhibit_index, name='exhibit_index'),
    path('<int:exhibit_id>/', views.exhibit_detail)
]