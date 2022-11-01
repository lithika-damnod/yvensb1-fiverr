from django.db import models
from django.utils import timezone


class Ad(models.Model):
    a_id = models.AutoField(primary_key=True)
    title = models.TextField(blank=False)
    description = models.TextField()
    price_per_km = models.IntegerField(blank=False)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    posted_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"ad_id: {self.a_id}, title: {self.title}, price_per_km: {self.price_per_km}"


class Car(models.Model):
    c_id = models.AutoField(primary_key=True)
    model = models.TextField(max_length=20, blank=False)
    brand = models.CharField(max_length=20, blank=False)
    number_plate = models.TextField(blank=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"car_id: {self.c_id}, brand: {self.brand}, model: {self.model}, plate_number: {self.number_plate}"


class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=10, blank=False)
    l_name = models.CharField(max_length=10, blank=False)
    age = models.IntegerField(blank=False)
    address_no = models.IntegerField(blank=False)
    address_street = models.TextField()
    address_city = models.TextField()
    address_country = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return f"u_id: {self.u_id}, f_name: {self.f_name}, l_name: {self.l_name}, age: {self.age}"
