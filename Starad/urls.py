from django.urls import path
# from .views import (
#     AboutListCreateView, AboutRetrieveUpdateDestroyView,
#     ServiceListCreateView, ServiceRetrieveUpdateDestroyView,
#     RecentWorkListCreateView, RecentWorkRetrieveUpdateDestroyView,
#     ContactMessageListCreateView, ContactMessageRetrieveUpdateDestroyView,
#     StudioListCreateView, StudioRetrieveUpdateDestroyView
# )
from Starad import views as starad_views



urlpatterns = [
    path('api/about/', starad_views.AboutListCreateView.as_view(), name='about-list-create'),
    path('api/about/<int:pk>/', starad_views.AboutRetrieveUpdateDestroyView.as_view(), name='about-detail'),
    
    path('api/services/', starad_views.ServiceListCreateView.as_view(), name='service-list-create'),
    path('api/services/<int:pk>/', starad_views.ServiceRetrieveUpdateDestroyView.as_view(), name='service-detail'),
    
    path('api/recent-works/', starad_views.RecentWorkListCreateView.as_view(), name='recentwork-list-create'),
    path('api/recent-works/<int:pk>/', starad_views.RecentWorkRetrieveUpdateDestroyView.as_view(), name='recentwork-detail'),
    
    path('api/contact-messages/', starad_views.ContactMessageListCreateView.as_view(), name='contactmessage-list-create'),
    path('api/contact-messages/<int:pk>/', starad_views.ContactMessageRetrieveUpdateDestroyView.as_view(), name='contactmessage-detail'),
    
    path('api/studios/', starad_views.StudioListCreateView.as_view(), name='studio-list-create'),
    path('api/studios/<int:pk>/', starad_views.StudioRetrieveUpdateDestroyView.as_view(), name='studio-detail'),
]
