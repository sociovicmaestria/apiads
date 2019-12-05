from django.contrib import admin

# Register your models here.

from .models import Category, Commerce, CommerceAddress, Reward, RewardDetail

admin.site.register(Category)
admin.site.register(Commerce)
admin.site.register(CommerceAddress)
admin.site.register(Reward)
admin.site.register(RewardDetail)