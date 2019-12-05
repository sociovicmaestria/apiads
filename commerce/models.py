from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    active = models.BooleanField(default=True)
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='category_user_create')
    date_create = models.DateTimeField(auto_now_add=True)
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='category_user_update')
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

class Commerce(models.Model):
    name = models.CharField(max_length=100, default='')
    logo = models.CharField(max_length=250, default='')
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='commerce_user_create')
    date_create = models.DateTimeField(auto_now_add=True)
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='commerce_user_update')
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

class CommerceAddress(models.Model):
    description = models.CharField(max_length=150, default='')
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    active = models.BooleanField(default=True)
    commerce = models.ForeignKey(Commerce, on_delete=models.CASCADE, null=True)
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='commerce_address_user_create')
    date_create = models.DateTimeField(auto_now_add=True)
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='commerce_address_user_update')
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('description',)

class Reward(models.Model):
    name = models.CharField(max_length=150, default='')
    active = models.BooleanField(default=True)
    commerce = models.ForeignKey(Commerce, on_delete=models.CASCADE, null=True)
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reward_user_create')
    date_create = models.DateTimeField(auto_now_add=True)
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='reward_user_update')
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

class RewardDetail(models.Model):
    points =  models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    active = models.BooleanField(default=True)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, null=True)
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reward_detail_user_create')
    date_create = models.DateTimeField(auto_now_add=True)
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='reward_detail_user_update')
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)