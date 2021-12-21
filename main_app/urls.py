from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('about-us/', About.as_view(), name="about-us"),
    path('menu/', Menu.as_view(), name="menu"),
    path('gallery/', Gallery.as_view(), name="gallery"),
    path('login/', Login.as_view(), name="login"),
    path('registration/', Registration.as_view(), name="registration"),
    path('log-out', LogoutView.as_view(next_page="home"), name="exit"),

    path("tgbot/getcategories/", ProductsCategoryView.as_view()),
    path("tgbot/getproducts/", ProductsView.as_view()),
    path("tgbot/orders/", order_products),
]