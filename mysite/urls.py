from django.contrib import admin
from django.urls import path, include
from .views import index, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('', include('mysiteapp.urls')),
    path('blog/', include('blog.urls')),
    path('login/', login, name="login")
]
