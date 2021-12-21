from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/<slug:slug>/', ArticleDetail.as_view() , name="blog"),
    path('blogs/', ArticlesList.as_view(), name="blogs"),
]