from rest_framework import routers

from user import viewsets as user_viewsets
from dashboards import viewsets as dashboard_viewsets

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'user', user_viewsets.UserViewSet, basename='user')
api.register(r'dashboards/manager', dashboard_viewsets.DashboardManagerViewSet, basename='dashboard-manager')
api.register(r'dashboards/viewer', dashboard_viewsets.DashboardManagerViewSet, basename='dashboard-viewer')
api.register(r'laptops', dashboard_viewsets.LaptopsViewSet, basename='laptops')