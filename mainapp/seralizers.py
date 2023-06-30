from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email','password','tc')
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ProductSerializer(serializers.ModelSerializer):
    UserSerializer()
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image','seller')

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('id', 'product','seller',  'buyer', 'purchase_price')


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields=['email','password']   
        
        
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['email', 'name','password','tc']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)             
