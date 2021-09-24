from django.core.validators import RegexValidator
from django.db import models


class Company(models.Model):
    user = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    billing_email = models.EmailField(max_length=225)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address_one = models.CharField(max_length=225, blank=True)
    address_two = models.CharField(max_length=225, blank=True)
    city = models.CharField(max_length=225, blank=True)
    country = models.CharField(max_length=225, blank=True)
    postal_code = models.CharField(max_length=225, blank=True)
