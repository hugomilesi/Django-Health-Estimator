# Generated by Django 5.1.3 on 2024-11-25 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('age', models.IntegerField()),
                ('region', models.CharField(choices=[('northwest', 'Northwest'), ('northeast', 'Northeast'), ('southwest', 'Southwest'), ('southeast', 'Southeast')], max_length=15)),
                ('children', models.IntegerField()),
                ('smoker', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('bmi', models.FloatField()),
                ('predicted_cost', models.FloatField(null=True)),
            ],
        ),
    ]