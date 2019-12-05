from rest_framework import serializers
from commerce.models import Category, Commerce, CommerceAddress, Reward, RewardDetail

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class CommerceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Commerce
        fields = ('id','name', 'logo', 'category_id', 'category')

class CommerceAddressSerializer(serializers.ModelSerializer):
    commerce = CommerceSerializer(read_only=True)
    commerce_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = CommerceAddress
        fields = ('id','description', 'latitude', 'longitude', 'commerce_id', 'commerce')

class RewardSerializer(serializers.ModelSerializer):
    commerce = CommerceSerializer(read_only=True)
    commerce_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Reward
        fields = ('id','name', 'commerce_id', 'commerce')

class RewardDetailSerializer(serializers.ModelSerializer):
    reward = RewardSerializer(read_only=True)
    reward_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = RewardDetail
        fields = ('id', 'points', 'start_date', 'end_date', 'reward_id', 'reward')