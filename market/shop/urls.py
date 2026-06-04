
# from django.urls import path , include
# from . import views
from django.urls import path
from . import views

# urlpatterns = [
    
#     path('' , include('shop.urls')),
#  ]
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]