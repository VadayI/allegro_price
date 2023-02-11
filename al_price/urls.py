from django.urls import path
from . import views

app_name = 'al_price'

urlpatterns = [
    path('get_allegro_price/<str:ean>', views.get_allegro_price, name='get_allegro_price'),
]