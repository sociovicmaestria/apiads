from rest_framework import serializers
from account.models import Customer, Account, Transaction, Exchange
from authorization.serializers import UserSerializer
from commerce.serializers import CommerceSerializer, RewardDetailSerializer

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'full_name', 'cellphone', 'user_id', 'user')

class AccountSerializer(serializers.ModelSerializer):
    commerce = CommerceSerializer(read_only=True)
    commerce_id = serializers.IntegerField(write_only=True)
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'total_points', 'total_visits', 'first_joined', 'commerce_id', 'commerce', 'customer_id', 'customer')

class TransactionSerializer(serializers.ModelSerializer):
    account = CommerceSerializer(read_only=True)
    account_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'ticket_number', 'ticket_date', 'amount', 'total_points', 'transaction_date', 'account_id', 'account')

class ExchangeSerializer(serializers.ModelSerializer):
    account = CommerceSerializer(read_only=True)
    account_id = serializers.IntegerField(write_only=True)
    reward_detail = RewardDetailSerializer(read_only=True)
    reward_detail_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'exchange_date', 'total_points', 'account_id', 'account', 'reward_detail_id', 'reward_detail')