from rest_framework import routers

from user import viewsets as user_viewsets

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'user', user_viewsets.UserViewSet, basename='user')