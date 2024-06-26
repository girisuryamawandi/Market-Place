from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('detail/<int:pk>/',views.detail,name="detail"),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('items/',views.items,name="items"),
    path('new/',views.new,name="new"),
]