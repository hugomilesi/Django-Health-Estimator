from django.db import models

# Create your models here.
class Prediction(models.Model):
    SEX_CHOICES = [('male', 'Male'), ('female', 'Female')]
    REGION_CHOICES = [
        ('northwest', 'Northwest'),
        ('northeast', 'Northeast'),
        ('southwest', 'Southwest'),
        ('southeast', 'Southeast'),
    ]
    SMOKER_CHOICES = [('yes', 'Yes'), ('no', 'No')]

    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    age = models.IntegerField()
    region = models.CharField(max_length=15, choices=REGION_CHOICES)
    children = models.IntegerField()
    smoker = models.CharField(max_length=3, choices=SMOKER_CHOICES)
    bmi = models.FloatField()

    def __str__(self):
        return f"{self.sex}, {self.age} years"
