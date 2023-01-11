from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class dish(models.Model):
    id = models.IntegerField(
            primary_key=True,
            validators=[MinValueValidator(1), MaxValueValidator(1000)]
            )
    type = models.CharField(max_length=10)
    img = models.ImageField(
            upload_to='test', 
            height_field=256,
            width_field=256
            )


class product(models.Model):
    id = models.IntegerField(
            primary_key=True,
            validators=[MinValueValidator(1), MaxValueValidator(100000)]
            )
    name = models.CharField(max_length=30)
    weight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000)])
    calories = models.IntegerField(validators=[MinValueValidator(30), MaxValueValidator(10000)])
    price = models.DecimalField(max_digits=6, decimal_places=2)


class recipe(models.Model):
    id = models.IntegerField(
            primary_key=True,
            validators=[MinValueValidator(1), MaxValueValidator(1000)]
            )
    name = models.CharField(max_length=30)
    cooking_time = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(90)])
    cooking_technology = models.CharField(max_length=1000)


class DishComposition(models.Model):
    dish_id = models.IntegerField(
            primary_key=True,
            validators=[MinValueValidator(1), MaxValueValidator(1000)]
            )
    product_id = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000)])
    product_count = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])


class DailyReport(models.Model):
    date = models.DateField(primary_key=True)
    dish_name = models.CharField(max_length=30)
    dish_id = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    count_of_cooked_dishes = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)])
