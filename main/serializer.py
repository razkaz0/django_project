from rest_framework import serializers
from .models import *
class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
class RoomsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomsCategory
        fields = '__all__'
class RoomsConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomsCondition
        fields = '__all__'
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
class EmployessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employess
        fields = '__all__'
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'