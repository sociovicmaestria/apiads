from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from account.models import Customer, Account, Transaction, Exchange
from account.serializers import CustomerSerializer, AccountSerializer, TransactionSerializer, ExchangeSerializer

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('id','full_name')
    ordering_fields = ('id','full_name')

    def perform_create(self, serializer):
        serializer.save(user_create=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user_update=self.request.user)

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('id','total_points')
    ordering_fields = ('id','total_points')

    def perform_create(self, serializer):
        serializer.save(user_create=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user_update=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('id','ticket_number')
    ordering_fields = ('id','ticket_number')

    def perform_create(self, serializer):
        serializer.save(user_create=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user_update=self.request.user)

class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('id','exchange_date')
    ordering_fields = ('id','exchange_date')

    def perform_create(self, serializer):
        serializer.save(user_create=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user_update=self.request.user)