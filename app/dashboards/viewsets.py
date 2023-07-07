from commons import viewsets
from dashboards import models
from dashboards import serializers
from rest_access_policy import AccessViewSetMixin
from dashboards import policies


class DashboardManagerViewSet(AccessViewSetMixin, viewsets.ModelViewSet):
    queryset = models.Dashboard.objects.all()
    access_policy = policies.DashBoardManagerPolicy

    def get_serializer_class(self):
        if self.action in ('retrieve',):
            return serializers.DashboardDetailSerializer
        return serializers.DashboardListSerializer

    def get_queryset(self):
        return self.access_policy.scope_queryset(self.request, self.queryset)


class DashboardsViewerViewSet(
    AccessViewSetMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = models.Dashboard.objects.filter(is_published=True)
    access_policy = policies.DashBoardViewerPolicy

    def get_serializer_class(self):
        if self.action in ('retrieve',):
            return serializers.DashboardDetailSerializer
        return serializers.DashboardListSerializer

    def get_queryset(self):
        return self.access_policy.scope_queryset(self.request, self.queryset)


class LaptopsViewSet(AccessViewSetMixin, viewsets.ReadOnlyModelViewSet):
    queryset = models.Laptops.objects.all()
    access_policy = policies.LaptopsPolicy
    serializer_class = serializers.LaptopsSerializer

    def get_queryset(self):
        return self.access_policy.scope_queryset(self.request, self.queryset)
