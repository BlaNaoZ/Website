from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_foundation_industries = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_heat_buyer = models.BooleanField(default=False)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class FoundationIndustries(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class HeatBuyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)