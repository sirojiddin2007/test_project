from django.urls import *
from .views import *


urlpatterns = [
    path('index/', index_view, name="index_url"),
    path('', signup_view, name="signup_url"),
    path('login/', signin_view, name="login_url"),
    path('logout/', logout_view, name="logout_url"),
    path('myprofile/', myprofile_view, name="myprofile_url"),
    path('menu/', menu_view, name='menu_page_url'),
    path('service/', service_view, name='services_page_url'),
    path('block/', blog_view, name='block_page_url'),
    path('about/', about_view, name='about_page_url'),
    path('block-single/', blog_single_view, name='block_single_page_url'),
    path('contact/', contact_view, name='contact_page_url'),
    path('category/<int:pk>/', filter_meal_by_category, name='filter_meal_by_category_url'),
]