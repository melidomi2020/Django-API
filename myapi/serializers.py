from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Hero
class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Hero
        fields=('id','name','alias')