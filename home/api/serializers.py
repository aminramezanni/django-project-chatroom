from rest_framework.serializers import ModelSerializer
from home.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'