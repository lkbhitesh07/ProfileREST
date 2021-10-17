from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from .views import ProfileView, OnlyPausedProfileView, PauseAProfileView, UnpauseAProfileView, CreateProfileView, DeleteProfileView

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='doc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('all-profiles/', ProfileView.as_view(), name='profile_view'),
    path('only-paused-profiles/', OnlyPausedProfileView.as_view(), name='only_paused_profile_view'),
    path('pause-a-profile/<str:name>/', PauseAProfileView.as_view(), name='pause_a_profile_view'),
    path('unpause-a-profile/<str:name>/', UnpauseAProfileView.as_view(), name='unpause_a_profile_view'),
    path('create-profiles/', CreateProfileView.as_view(), name='create_profile_view'),
    path('delete-profiles/<str:name>/', DeleteProfileView.as_view(), name='delete_profile_view'),
]