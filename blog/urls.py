from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_post, name='add_post'),
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>',views.detail,name='post_detail'),
    path('<slug:slug>/',views.category,name='category_detail'),
]
