from rest_framework import serializers
from authorization.models import User
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','password','email','groups','activate')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)        
        user.save()
        return user

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name')