from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField("Ovqat turi", max_length=150)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField("Ovqat nomi", max_length=150)
    category = models.ForeignKey(Category, related_name="foods", on_delete=models.CASCADE)
    image = models.ImageField("Rasmi", upload_to="foods_image/")
    SALE_TYPES = (
        ('qt', 'quantity'),# soni
        ('wg', 'weight'),# og'irligi
        ('sv', 'serving'),# porsiya
    )
    sale_type = models.CharField(choices=SALE_TYPES, max_length=50)
    price = models.PositiveIntegerField("Narxi (so`mda)")
    price_discounted = models.PositiveIntegerField("Chegirmali narxi", blank=True, null=True)
    info = models.TextField("Malumoti")

    def __str__(self):
        return self.name
