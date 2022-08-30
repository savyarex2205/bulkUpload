from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import userModel

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = "__all__"