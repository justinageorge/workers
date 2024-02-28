from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import workerModelViewsetView
router=DefaultRouter()

router.register("v2/workers/",workerModelViewsetView,basename="workers")
urlpatterns=[

]+router.urls