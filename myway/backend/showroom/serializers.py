from rest_framework import serializers
from .models import Car

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework.decorators import api_view
from rest_framework.response import Response

class CarSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = '__all__'

    def get_image(self, obj):
        if not obj.image or not hasattr(obj.image, 'url'):
            return None
        url = obj.image.url
        if url.startswith('http://') or url.startswith('https://'):
            return url
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(url)
        return url


####
class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class OrderSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()




@api_view(['POST'])
def request_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        return Response({'status': 'success'})
    return Response(serializer.errors, status=400)