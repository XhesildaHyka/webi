from django.urls import path
from . import views
urlpatterns = [
    path("", views.home,name="homepage"),
    path("contact/", views.contact, name="contactpage"),
    path("about/", views.about, name="aboutpage"),
    path("details/<int:id>", views.details, name="detailspage"),
    path("kategori/<int:id>", views.kategori, name="kategoripage"),
    path("item/<int:id>", views.item, name="itempage"),
    path("arrival/<int:id>", views.arrival, name="arrivalpage"),
    


]
