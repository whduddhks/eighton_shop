from django.urls import path, include
from . import views
#

urlpatterns = [
    path('', views.home, name="home"),
    path('pageone/', views.pageone, name="pageone"),
    path('pagetwo/', views.pageone, name="pagetwo"),
    path('pagethree/', views.pageone, name="pagethree"),
    path('pagefour/', views.pageone, name="pagefour"),
    path('pagefive/', views.pageone, name="pagefive"),
    path('basket/', views.basket, name="basket"),
    path('success/', views.success, name="success"),
    path('pageonedetail/', views.pageone, name="pageonedetail"),
    path('pagetwodetail/', views.pageone, name="pagetwodetail"),
    path('pagethreedetail/', views.pageone, name="pagethreedetail"),
    path('pagefourdetail/', views.pageone, name="pagefourdetail"),
    path('pagefivedetail/', views.pageone, name="pagefivedetail"),
    path('list/', views.product_list),
    path('write/', views.prodcut_write),
    path('list/<int:pk>/', views.product_detail),
]
