from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('list/', views.category_list, name='list'),
    path('detail/<int:pk>/', views.category_detail, name='detail'),
    path('create/', views.category_create, name='create'),
    path('update/<int:pk>/', views.category_update, name='update'),
    path('delete/<int:pk>/', views.category_delete, name='delete'),
]
