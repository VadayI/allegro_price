from django.db import models
from django.db.models.fields import CharField

DEF_ALLEGRO_PATH = 'https://allegro.pl/listing?string={}&order=p'

class Settings(models.Model):

    allegro_path = CharField(max_length=2000, default=DEF_ALLEGRO_PATH, blank=False, null=False)

    class Meta:
        verbose_name = 'Ustawienie Ogólne'
        verbose_name_plural = 'Ustawienia Ogólne'
