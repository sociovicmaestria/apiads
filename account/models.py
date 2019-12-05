from django.db import models
from django.conf import settings
from authorization.models import User
from commerce.models import Commerce, RewardDetail

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Customer(models.Model):
    full_name = models.CharField(max_length=150, default='')
    cellphone = models.CharField(max_length=20, default='', null=True)
    birthdate = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer_user_create')
    date_create = models.DateTimeField(auto_now_add=True)
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='customer_user_update')
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('full_name',)

class Account(models.Model):
    total_points = models.IntegerField(null=True)
    total_visits = models.IntegerField(null=True)
    first_joined = models.DateField(null=True)
    commerce = models.ForeignKey(Commerce, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='account_user_create')
    date_create = models.DateTimeField(auto_now_add=True)
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='account_user_update')
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('total_points',)

class Transaction(models.Model):
    ticket_number = models.CharField(max_length=50, default='')
    ticket_date = models.DateField(null=True)
    amount = models.FloatField(null=True)
    total_points = models.IntegerField(null=True)
    transaction_date = models.DateTimeField(null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transaction_user_create')
    date_create = models.DateTimeField(auto_now_add=True)
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='transaction_user_update')
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('ticket_date',)

class Exchange(models.Model):
    exchange_date = models.DateTimeField(null=True)
    total_points = models.IntegerField(null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    reward_detail = models.ForeignKey(RewardDetail, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exchange_user_create')
    date_create = models.DateTimeField(auto_now_add=True)
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='exchange_user_update')
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('exchange_date',)