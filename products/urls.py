from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('list/', views.product_list, name='list'),
    # path('detail/<int:pk>/', views.product_detail, name='detail'),
    path('create/', views.product_create, name='create'),
    # path('update/<int:pk>/', views.product_update, name='update'),
    # path('delete/<int:pk>/', views.product_delete, name='delete'),
]
