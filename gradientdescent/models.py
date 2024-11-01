from django.db import models


# Create your models here.
class Monarch(models.Model):
    campaign_name = models.SlugField("Campaign name", unique=True)
    current_stress = models.IntegerField("Monarch Current Stress Level", default=0)

    def __str__(self):
        return f"{self.campaign_name}: current stress: {self.current_stress}."
