from django.urls import path
from .views import home_view,contact_view,service_view,guard_view,about_view



urlpatterns = [
    path('',home_view,name="home-page"),
    path('about/',about_view,name="about-page"),
    path('guard/',guard_view,name="guard-page"),
    path('contact/',contact_view,name="contact-page"),
    path('service/',service_view,name="service-page"),
]



