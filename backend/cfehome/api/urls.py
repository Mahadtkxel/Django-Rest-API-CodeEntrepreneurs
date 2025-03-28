from django.urls import path
from . import views
# roughly same as above
# from .views import api_home


urlpatterns = [
    path('', views.api_home, name="api_home"),
]
