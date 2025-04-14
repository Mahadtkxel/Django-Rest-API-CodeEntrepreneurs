from django.urls import path, include
from . import views
# roughly same as above
# from .views import api_home


urlpatterns = [
    path('', views.api_home, name="api_home"), # localhost:8000/api/
    # path('products/', include('products.urls'))
]
