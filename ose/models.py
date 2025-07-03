from django.db import models

# Create your models here.


class Monster(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    ac = models.CharField(max_length=20)
    hit_dice = models.CharField(max_length=20)
    attacks = models.CharField(max_length=200, null=True, blank=True)
    thac0 = models.CharField(max_length=12)
    movement = models.CharField(max_length=200)
    saving_throws = models.CharField(max_length=200)
    morale = models.CharField(max_length=100)
    alignment = models.CharField(max_length=100)
    xp = models.CharField(max_length=100)
    number_appearing = models.CharField(max_length=100)
    treasure_type = models.CharField(max_length=100, null=True, blank=True)
    extra_info = models.TextField(max_length=2000, null=True, blank=True)
    source = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.name}."
