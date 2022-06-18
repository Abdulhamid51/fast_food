from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import *
from .serializers import *
from accounts.models import *

@api_view(['GET'])
def index_view(request):
    subcategory = request.GET.get('category')
    if subcategory:
        obj = Food.objects.filter(subcategory=subcategory)
    else:
        obj = Food.objects.all()
    serializer = FoodSerializer(obj, many=True)
    return Response({'response':serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_cart(request):
    food = Food.objects.get(id=int(request.data['food_id']))
    cart = Cart.objects.create(
        user=request.user,
        food=food
    )
    if food.sale_type == 'qt':
        cart.quantity = int(request.data['nums'])
    elif food.sale_type == 'wg':
        cart.weight = float(request.data['nums'])
    else:
        cart.serving = float(request.data['nums'])
    cart.save()
    return Response({"result":"ok"})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_cart(request):
    cart = Cart.objects.get(id=request.data['cart_id'])
    if cart.quantity:
        cart.quantity = request.data['nums']
    elif cart.weight:
        cart.weight = request.data['nums']
    else:
        cart.serving = request.data['nums']
    cart.save()
    return Response({"result":"ok"})