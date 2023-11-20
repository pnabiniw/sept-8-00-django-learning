# Single, multiple, multilevel, hierarchical, hybrid
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


class ListUpdateViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    pass


class CreateRetrieveUpdateViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    pass
