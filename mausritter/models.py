from django.db import models


class Creature(models.Model):
    name = models.CharField(max_length=60)
    HP = models.IntegerField()
    STR = models.IntegerField()
    DEX = models.IntegerField()
    WIL = models.IntegerField()
    armor = models.IntegerField(null=True, blank=True)
    attack1 = models.CharField(blank=True, max_length=60)
    attack2 = models.CharField(blank=True, max_length=60)
    crit = models.TextField(blank=True)
    special = models.TextField(blank=True)
    spells = models.CharField(blank=True, max_length=60)
    wants = models.TextField(blank=True)
    variation_name = models.CharField(blank=True, max_length=60)
    # variation_text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}."


class Variation(models.Model):
    creature = models.ForeignKey(Creature, on_delete=models.CASCADE)
    first_part = models.CharField(max_length=200)
    last_part = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_part} {self.last_part}"
