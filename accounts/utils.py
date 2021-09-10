from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import serializers


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please check and try again!")
    return user

def create_user_account(
    email,
    first_name,
    last_name,
    password,
    **extra_fields
    ):
    user = get_user_model().objects.create_user(
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password,
         **extra_fields)
    return user