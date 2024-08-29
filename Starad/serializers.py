from rest_framework import serializers
from Starad import models as starad_model
# from .models import About, Service, RecentWork, ContactMessage, Studio


# About Serializer
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = starad_model.About
        fields = '__all__'

    # To Show the Image on the Api
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


# Service Serializer
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = starad_model.Service
        fields = '__all__'


# RecentWork Serializer
class RecentWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = starad_model.RecentWork
        fields = '__all__'

    # To Show the Image on the Api
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


# COntact Serializer
class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = starad_model.ContactMessage
        fields = '__all__'


# Studio Serializer
class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = starad_model.Studio
        fields = '__all__'

    # To Show the Image on the Api
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

