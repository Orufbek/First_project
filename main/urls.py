from django.urls import path
from .views import *

urlpatterns = [
    path('index', index_view, name="index_url"),
    path('', login_view, name="login_url"),
    path('register_url/', register_view, name="register_url"),
    path('filter_meal_by_category/<int:id>/', filter_meal_by_category, name="filter_meal_by_category_url"),
    path('new_contact_us/', new_contact_us, name="contact_us_url"),
    path('menu/', menu_view, name="menu_url"),
    path('contact/', contact_view, name="contact_url"),
    path('about/', about_view, name="about_url"),
    path('services/', services_view, name="services_url"),
    path('blog/', blog_view, name='blog_url'),
    path('may_profile/', my_profile, name='my_profile_url'),
    path('log_out/', log_out_view, name='log_out_url'),
    path('edit_user/<int:id>/', edit_user_view, name='edit_user_url'),
    path('blog-single', blog_singe_view, name='single_blog_url'),
    path('create_message/<int:pk>/', create_message, name='create_message_url'),

]