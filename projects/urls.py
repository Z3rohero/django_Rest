# paa hacer mi rutas , djangoframewok ya tiene rutas ya realizadas
from rest_framework import routers
from .api import ProjectViewSet 

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet , 'project')

urlpatterns = router.urls