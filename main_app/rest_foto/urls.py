from django.urls import path, include

from . import views

app_name = 'rest_foto'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('new_image/', views.new_image, name='new_image'),
    path('filter_foto/', views.filter_foto, name='filter_foto'),
    path('<int:foto_id>/', views.foto, name='foto'),
]