from rest_framework import serializers
from .models import User,Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ['id', 'name', 'email']

    def validate_email(self, value):
        """Ensure email is unique"""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price']    