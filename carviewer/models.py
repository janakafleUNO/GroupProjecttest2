from django.db import models
from django.utils import timezone


# Define the model for the CarViewer table


class CarBrand(models.Model):
    car_brand = models.CharField(max_length=50)
    car_year = models.CharField(max_length=50)
    car_image = models.ImageField(upload_to='cars/%Y/%M/%D', blank=True)

    def __str__(self):
        return self.car_brand


class CarType(models.Model):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cartypes', default=True)
    car_image = models.ImageField(upload_to='cars/%Y/%M/%D', blank=True)
    car_bodytype = models.CharField(max_length=50)
    car_fueltype = models.CharField(max_length=50)
    car_transmission = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.car_brand)


class CarModel(models.Model):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='carmodels', default=True)
    car_year = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    car_image = models.ImageField(upload_to='cars/%Y/%M/%D', blank=True)
    car_bodytype = models.CharField(max_length=50)
    car_fueltype = models.CharField(max_length=50)
    car_transmission = models.CharField(max_length=50)
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    car_mileage = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.car_brand)


class CarReview(models.Model):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='carreviews', default=True)
    car_year = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    car_image = models.ImageField(upload_to='cars/%Y/%M/%D', blank=True)
    car_bodytype = models.CharField(max_length=50)
    car_expert_review = models.CharField(max_length=100)
    car_user_review = models.CharField(max_length=100)
    car_overall_review = models.CharField(max_length=100)

    def __str__(self):
        return str(self.car_brand)
