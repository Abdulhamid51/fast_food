from rest_framework import serializers
from .models import *
from accounts.models import *


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)

    class Meta:
        model = Food
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    food = FoodSerializer(many=False)
    class Meta:
        model = Cart
        fields = '__all__'