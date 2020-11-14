from event_management.viewsets import EventsViewset, UserViewset
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('event', EventsViewset)

router.register('user', UserViewset)