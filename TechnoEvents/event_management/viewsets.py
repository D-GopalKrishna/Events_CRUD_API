from rest_framework import viewsets
from . import models
from . import serializers

class EventsViewset(viewsets.ModelViewSet):
    queryset = models.Events.objects.all()
    serializer_class = serializers.EventsSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    