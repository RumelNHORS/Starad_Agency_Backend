from rest_framework import generics
# from .models import About, Service, RecentWork, ContactMessage, Studio
from Starad import models as starad_models
# from .serializers import AboutSerializer, ServiceSerializer, RecentWorkSerializer, ContactMessageSerializer, StudioSerializer
from Starad import serializers as starad_serializers




# About Views
class AboutListCreateView(generics.ListCreateAPIView):
    queryset = starad_models.About.objects.all()
    serializer_class = starad_serializers.AboutSerializer


# About Update Views
class AboutRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = starad_models.About.objects.all()
    serializer_class = starad_serializers.AboutSerializer


# Service Views
class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = starad_models.Service.objects.all()
    serializer_class = starad_serializers.ServiceSerializer


# Service Update Views
class ServiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = starad_models.Service.objects.all()
    serializer_class = starad_serializers.ServiceSerializer


# Recent Work Views
class RecentWorkListCreateView(generics.ListCreateAPIView):
    queryset = starad_models.RecentWork.objects.all()
    serializer_class = starad_serializers.RecentWorkSerializer


# Recent Work Update Views
class RecentWorkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = starad_models.RecentWork.objects.all()
    serializer_class = starad_serializers.RecentWorkSerializer


# Contact Message Views
class ContactMessageListCreateView(generics.ListCreateAPIView):
    queryset = starad_models.ContactMessage.objects.all()
    serializer_class = starad_serializers.ContactMessageSerializer


# Contact Message Update Views
class ContactMessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = starad_models.ContactMessage.objects.all()
    serializer_class = starad_serializers.ContactMessageSerializer


# Studio Views
class StudioListCreateView(generics.ListCreateAPIView):
    queryset = starad_models.Studio.objects.all()
    serializer_class = starad_serializers.StudioSerializer


# Studio Update Views
class StudioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = starad_models.Studio.objects.all()
    serializer_class = starad_serializers.StudioSerializer
