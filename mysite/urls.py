from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth.views import LogoutView
from .views import index, login, custom_logout, signup, contact, Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('', include('mysiteapp.urls')),
    path('blog/', include('blog.urls')),
    path('login/', Login.as_view(), name="login"),
    path('logout/', custom_logout, name="logout"),
    path('signup/', signup, name="signup"),
    path('contact/', contact, name="contact")
]
