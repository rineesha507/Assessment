from django.shortcuts import render
from django.http import HttpResponse
from .utils import reverse  
from rest_framework import viewsets
from .models import User,Product
from .serializers import UserSerializer,ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response




def reverse_view(request):
    text = "Hello World Python"
    reversed_text = reverse(text)
    return HttpResponse(reversed_text) 

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


@api_view(['GET'])
def top_expensive_products(request):
    """Fetch the top 3 most expensive products"""
    top_products = Product.objects.order_by('-price')[:3]  # Sorting by price (desc)
    serializer = ProductSerializer(top_products, many=True)
    return Response(serializer.data)