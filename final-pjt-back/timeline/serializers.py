from rest_framework import serializers
from .models import Timeline
from django.contrib.auth import get_user_model

class TimelineListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timeline
        fields = '__all__'