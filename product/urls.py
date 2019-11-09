from django.urls import path, include
from . import views
#

urlpatterns = [
    path('', views.home, name="home"),
    path('pageone/', views.pageone, name="pageone"),
    path('pagetwo/', views.pagetwo, name="pagetwo"),
    path('pagethree/', views.pagethree, name="pagethree"),
    path('pagefour/', views.pagefour, name="pagefour"),
    path('pagefive/', views.pagefive, name="pagefive"),
    path('basket/', views.basket, name="basket"),
    path('success/', views.success, name="success"),
    path('pageonedetail/', views.pageonedetail, name="pageonedetail"),
    path('pagetwodetail/', views.pagetwodetail, name="pagetwodetail"),
    path('pagethreedetail/', views.pagethreedetail, name="pagethreedetail"),
    path('pagefourdetail/', views.pagefourdetail, name="pagefourdetail"),
    path('pagefivedetail/', views.pagefivedetail, name="pagefivedetail"),
    path('list/', views.product_list),
    path('write/', views.prodcut_write),
    path('list/<int:pk>/', views.product_detail),
]
