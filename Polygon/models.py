from django.contrib.gis.db import models

class Polygone(models.Model):
    location = models.PolygonField()



