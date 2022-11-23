from django.shortcuts import render,get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TimelineListSerializer
from .models import Timeline

# Create your views here.

@api_view(['GET'])
def get_list(request, user_id):
    lines = Timeline.objects.filter(follower_id=user_id)
    serializer = TimelineListSerializer(lines, many=True)
    response = serializer.data[-1:-11:-1]
    for line in lines:
        line.is_checked = True
        line.save()
    return Response(response)