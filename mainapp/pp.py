from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .seralizers import UserSerializer
from rest_framework.views import APIView
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .seralizers import ProductSerializer, PurchaseSerializer
from .models import Product, Purchase
from rest_framework.generics import CreateAPIView
from rest_framework.filters import  SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

def get_refresh_token(user):
    refresh=RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token), 
    }


class ProductCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[SearchFilter]
    search_fields=['user_name']

    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         product = serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)

class PurchaseCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            purchase = serializer.save(product=product, seller=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProductListAPIView(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        product = Product.objects.filter(pk=pk)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)    


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class registartion(CreateAPIView):
    queryset=User
    serializer_class=UserSerializer



class UserAuthenticationAPIView(APIView):
    def post(self, request):
        email = request.data.get('username')
        password = request.data.get('password')
        (email,password)
        user = authenticate(email=email, password=password)
        # if user is not None:
        #     payload = jwt_payload_handler(user)
        #     token = jwt_encode_handler(payload)
        #     return Response({'token': token})
        # return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        if user is not None:
            token = get_refresh_token(user)
            return Response({'token':token,'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}},
                status=status.HTTP_404_NOT_FOUND) 
   
