from django.contrib import admin
from django.urls import path, include
import product.views
# user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', include('user.urls')),
    path('', include('product.urls')),

]
