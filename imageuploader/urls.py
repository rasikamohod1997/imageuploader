from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('emp_login/', emp_login, name='emp_login'),
    path('home/', home, name='home'),
    path('logout/', Logout, name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

