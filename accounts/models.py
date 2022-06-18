from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", verbose_name="User", on_delete=models.CASCADE)
    birth_date = models.DateField("Tug`ulgan sanasi", blank=True, null=True)
    location = models.CharField("Lakatsiyasi", max_length=400, blank=True, null=True)
    gender = models.CharField("Jinsi male/female", max_length=6, blank=True, null=True)
    avatar = models.ImageField("Rasmi", upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_Profile(sender, instance, created, **kwargs):
    if created == True:
        Profile.objects.create(user=instance)


class Cart(models.Model):
    user = models.ForeignKey(User, related_name="carts", on_delete=models.CASCADE)
    food = models.ForeignKey("api.Food", related_name="food_carts", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Soni", blank=True, null=True)
    weight = models.FloatField("Og`irligi", blank=True, null=True)
    serving = models.FloatField("Porsiya", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ga {self.food.name}"