from rest_framework import serializers
from .models import *


class RadiDeptSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return RadiDept.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)


class RadiTestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiTestCategory


class RadiTestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiTestType