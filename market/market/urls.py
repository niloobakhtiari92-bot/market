
# from django.contrib import admin
# from django.urls import path , include
# from .import settings
# from django.conf.urls.static import static 
# from django.conf import settings
# import os


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('' , include('shop.urls')),
# ]#+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

# # # این خط را حتماً اضافه کنید:
# # if settings.DEBUG:
# #     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# #     # اگر STATIC_ROOT ندارید، از خط زیر استفاده کنید:
# #     urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))  
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
##########################################################
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop.views import product_list, product_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'),
    path('<int:product_id>/', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)