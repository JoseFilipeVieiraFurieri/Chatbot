from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='chat'),
    path('teste', views.test, name="urlTeste"),

    path("getResponse", views.getResponse, name="Response")
]