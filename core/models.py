from django.db import models
from django.contrib.auth.models import User

class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, blank=True)
    membership_level = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Vendor: {self.user.username}"

class Product(models.Model):
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=100, default='Available')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
