from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

REQUEST_STATUS = ((0, 'Pending'), (1, 'Approved'), (3, 'Denied'))


class Booking(models.Model):
    booking_date = models.DateField()
    party_of = models.IntegerField(
        default=2,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
     )
    notes = models.CharField(max_length=500)
    reference = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices=REQUEST_STATUS, default=0)


class Meta:
    ordering = ['-created_on']


def __str__(self):
    return self.reference
