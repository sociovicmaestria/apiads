from django.shortcuts import render
from rest_framework import viewsets
from authorization.models import User
from django.contrib.auth.models import Group
from authorization.serializers import UserSerializer, GroupSerializer
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('username', 'email')
    ordering_fields = ('username', 'email')

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('id','name')
    ordering_fields = ('id','name')