from django.db import models
from django.contrib.gis.db import models
import geocoder

# Create your models here.

access_token='pk.eyJ1IjoiZWRpc29ubXNqIiwiYSI6ImNrcGhwaHhsaDBqcjUyb2xpaHB0czVvY3oifQ.xwV3-fok4T9Z6UI9YqUJDQ'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)


    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key = access_token)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)

class TestGeo(models.Model):
    name = models.CharField(max_length=25)  # corresponds to the 'str' field
    point = models.PointField(srid=4269)  # we want our model in a different SRID

    def __str__(self):
        return "Name: %s" % self.name