from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import verify_jwt_token



urlpatterns = [
    path('admin/', admin.site.urls),
                                                                                                                                
    path('auth/', include('djoser.urls')),
    path('api/', include('chat.urls'))
]