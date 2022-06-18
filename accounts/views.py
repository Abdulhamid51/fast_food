from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import *
from api.serializers import ProfileSerializer, CartSerializer

@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        key = Token.objects.get(user=user)
        return Response({"key":key.__str__()})
    else:
        return Response({"error":"username or password incorrect"})

@api_view(['POST'])
def register(request):
    username = request.data['username']
    password = request.data['password']
    user = User.objects.create_user(username=username, password=password)
    key = Token.objects.create(user=user)
    return Response({"key":key.__str__()})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    profile = Profile.objects.get(user=request.user)
    profile.birth_date = request.data['birth_date']
    profile.location = request.data['location']
    profile.gender = request.data['gender']
    profile.avatar = request.data['avatar']
    profile.save()
    serializer = ProfileSerializer(Profile.objects.get(user=request.user), many=False)
    return Response({"user":profile})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_detail(request):
    profile = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer(profile, many=False).data
    cart = Cart.objects.filter(user=request.user)
    cart_serializer = CartSerializer(cart, many=True).data
    serializer.update({
            "first_name":request.user.first_name,
            "last_name":request.user.last_name,
            "carts":cart_serializer
        })
    return Response(serializer)