from rest_framework import serializers
from .models import Car

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
        return url  # Если request нет, возвращаем как есть