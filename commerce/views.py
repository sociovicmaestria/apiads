from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from commerce.models import Category, Commerce, CommerceAddress, Reward, RewardDetail
from commerce.serializers import CategorySerializer, CommerceSerializer, CommerceAddressSerializer, RewardSerializer, RewardDetailSerializer


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('id','name')
    ordering_fields = ('id','name')

    def perform_create(self, serializer):
        serializer.save(user_create=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user_update=self.request.user)

class CommerceViewSet(viewsets.ModelViewSet):
    queryset = Commerce.objects.all()
    serializer_class = CommerceSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('id','name')
    ordering_fields = ('id','name')

    def perform_create(self, serializer):
        serializer.save(user_create=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user_update=self.request.user)

class CommerceAddressViewSet(viewsets.ModelViewSet):
    queryset = CommerceAddress.objects.all()
    serializer_class = CommerceAddressSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('id','description')
    ordering_fields = ('id','description')

    def perform_create(self, serializer):
        serializer.save(user_create=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user_update=self.request.user)

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('id','name')
    ordering_fields = ('id','name')

    def perform_create(self, serializer):
        serializer.save(user_create=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user_update=self.request.user)

class RewardDetailViewSet(viewsets.ModelViewSet):
    queryset = RewardDetail.objects.all()
    serializer_class = RewardDetailSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('id','start_date', 'end_date')
    ordering_fields = ('id','start_date', 'end_date')

    def perform_create(self, serializer):
        serializer.save(user_create=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user_update=self.request.user)