from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


INSTITUTIONS = (
    (1, 'fundacja'),
    (2, 'organizacja pozarządowa'),
    (3, 'zbiórka lokalna'),
)


class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.IntegerField(choices=INSTITUTIONS, default=1)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

