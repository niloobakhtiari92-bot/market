
from django.contrib import admin
from django.urls import path , include
from .import settings
from django.conf.urls.static import static 
import os


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('shop.urls')),
]#+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

# # این خط را حتماً اضافه کنید:
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     # اگر STATIC_ROOT ندارید، از خط زیر استفاده کنید:
#     urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))  