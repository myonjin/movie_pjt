from django.shortcuts import render

# permission Decorators
# view 함수에 @permission_classes([IsAuthenticated]) 데코레이터 달면
# 따로 인증 과정 필요함 (== 토큰 확인 == headers에 토큰 넣어서 요청보내야함)
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
