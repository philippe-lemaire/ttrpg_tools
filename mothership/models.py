from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Bounty(models.Model):

    target = models.CharField(blank=True, max_length=250)
    bounty_level = models.IntegerField(default=1)
    crime = models.CharField(blank=True, max_length=250)
    location = models.CharField(blank=True, max_length=250)
    client = models.CharField(blank=True, max_length=250)
    wanted = models.CharField(blank=True, max_length=50)
    reward = models.CharField(blank=True, max_length=250)
    bonus = models.CharField(blank=True, max_length=250)
    known_associates = models.CharField(blank=True, max_length=250)
    point_of_collection = models.CharField(blank=True, max_length=250)
    last_known_location = models.CharField(blank=True, max_length=250)
    advert = models.TextField(blank=True)
    briefing = HTMLField(blank=True, max_length=10000)
    warden_info = HTMLField(blank=True, max_length=10000)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f"Bounty for {self.target}. BL: {self.bounty_level}."
