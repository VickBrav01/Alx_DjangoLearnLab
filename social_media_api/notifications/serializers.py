from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_name = serializers.CharField(source='actor.username', read_only=True)
    target_object = serializers.CharField(source='target', read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'