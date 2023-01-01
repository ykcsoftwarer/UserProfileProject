from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse
# Create your views here.
from .serializers import UserProfileSerializer
from .models import UserProfile







@api_view()  # default GET
def user_home(requst):
    return HttpResponse({'home': 'This is user profile page...'})