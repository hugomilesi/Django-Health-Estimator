from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prediction_db(models.Model):
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
    predicted_cost = models.FloatField(null=True)

    def __str__(self):
        return f"{self.sex}, {self.age} sex"


class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)  # Replace 1 with your desired default user ID
    id = models.AutoField(primary_key=True)  # Explicitly defining auto-incrementing ID
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
    predicted_cost = models.FloatField(null=True)

    def __str__(self):
        return f"{self.sex}, {self.age} years"