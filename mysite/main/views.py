from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from django.http import HttpResponse
from .serializer import *

def index(request):
    return HttpResponse("<h4>Booking номеров</h4>")
class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
class RoomsCategoryViewSet(viewsets.ModelViewSet):
    queryset = RoomsCategory.objects.all()
    serializer_class = RoomsCategorySerializer
class RoomsConditionViewSet(viewsets.ModelViewSet):
    queryset = RoomsCondition.objects.all()
    serializer_class = RoomsConditionSerializer
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class EmployessViewSet(viewsets.ModelViewSet):
    queryset = Employess.objects.all()
    serializer_class = EmployessSerializer
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer





