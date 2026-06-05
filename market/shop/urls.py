from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),       # صفحه اصلی
    path('about/', views.about, name='about'),       # صفحه درباره ما
    # path('product/<int:pk>/', views.product_detail, name='product_detail'),  # جزئیات محصول
    path('login/', views.login_user, name='login'), 
    path('logout', views.logout_user, name='logout'), 
 ]