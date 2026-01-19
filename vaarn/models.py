from django.db import models


class Creature(models.Model):
    creature_types = (
        ("1", "Biological"),
        ("2", "Synthetic"),
        ("3", "Psychic"),
        ("4", "Fungal"),
        ("5", "Mineral"),
        ("6", "Hypergeometric"),
        ("7", "Outsider"),
    )
    name = models.CharField(max_length=60)
    creature_type = models.CharField(max_length=1, choices=creature_types)
    LVL = models.IntegerField()
    HP = models.IntegerField()
    AV = models.IntegerField()
    ML = models.IntegerField()
    Encountered = models.IntegerField()
    ATK = models.CharField(blank=True, max_length=250)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}."

    def __str__(self):
        return f"{self.name}, LVL {self.LVL}"
