from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home,name='home-page'),

    path('restaurant/', views.RestaurantListView.as_view(), name='restaurantList'),
    path('event/', views.EventListView.as_view(), name='event'),
    path('place/', views.PlacecListView.as_view(), name='place'),
    path('restaurant/<pk>', views.RestaurantDetail.as_view(), name='restaurant'),
    path('event/<pk>', views.EventDetail.as_view(), name='eve'),


]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)