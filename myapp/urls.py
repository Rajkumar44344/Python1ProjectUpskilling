from django.contrib import admin
from django.urls import path,include
from .views import *
import emp 
from django.conf import settings
from django.conf.urls.static import static

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
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
