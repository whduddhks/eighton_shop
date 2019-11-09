from django.urls import path, include
from . import views
#

urlpatterns = [
    path('order/', views.OrderCreate),
    path('order/list', views.OrderList),
]
