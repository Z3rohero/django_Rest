# paa hacer mi rutas , djangoframewok ya tiene rutas ya realizadas
#resst_framework ya viene instalando todo el crud para eliminar. 
#con router
from rest_framework import routers
from .api import ProjectViewSet 

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet , 'project')

urlpatterns = router.urls