from django.contrib import admin
from django.urls import path,include
from .views import *
import emp 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('home/', home, name='home'),  # Added name for redirection
    path('index/', home),
    path('services/', services),
    path('', register_view),
    path('login_view/', login_view, name='login'),  # Fixed name
    path('register/', register_view, name='register'),
    path("emp/",include('emp.urls'))
]
