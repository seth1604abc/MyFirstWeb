from django.urls import path
from . import views

urlpatterns = [
    path('', views.commodity, name='commodity'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('order/<int:pk>', views.order, name='order'),
    path('information/<int:pk>/', views.information, name='information'),
]