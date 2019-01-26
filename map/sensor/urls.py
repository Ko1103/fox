from rest_framework import routers
from .views import SensorViewset, ReferenceViewset

router = routers.DefaultRouter()
router.register(r'sensors', SensorViewset)
router.register(r'references', ReferenceViewset)
