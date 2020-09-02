from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="Aboutus"),
    path('contact/',views.contact, name="Contactus"),
    path('tracker/',views.tracker, name="TrackingStatus"),
    path('search/',views.search, name="Search"),
    path('productView/',views.productView, name="ProductViews"),
    path('checkout/',views.checkout, name="Checkout"),
]
