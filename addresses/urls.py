from django.urls import path
from .views import AddressView
from . import views

urlpatterns = [
    path('', AddressView.as_view(), name='home'),
    path('search/', views.search_place_view, name='search_place')

]