
# from django.urls import path , include
# from . import views
from django.urls import path
from .views import product_list , about

# urlpatterns = [
    
#     path('' , include('shop.urls')),
#  ]
urlpatterns = [
    path('', product_list , name="home"),
    # path('', product_detail),
    path('/about/' , about , name="about"),
]