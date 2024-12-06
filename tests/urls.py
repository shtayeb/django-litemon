from django.contrib import admin
from django.urls import path,include
from test_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("litemon/", include("django_litemon.urls")),
    path('admin/', admin.site.urls),
]