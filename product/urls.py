from django.urls import path, include
from . import views
#

urlpatterns = [
    path('list/', views.product_list),
    path('write/', views.prodcut_write),
    path('list/<int:pk>/', views.product_detail),
]
