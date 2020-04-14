from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.show_index)
]