from django.urls import path
from rest_framework import routers
from .views import bankviewsets,branchviewsets

router=routers.DefaultRouter()
router.register('Branch',branchviewsets)
urlpatterns = router.urls
