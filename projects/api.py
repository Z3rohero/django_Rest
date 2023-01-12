from .models import Project
from rest_framework  import  viewsets, permissions
from .serializers import ProjectSerializer

class ProjectSerializer(viewsets.ModelViewSet):
    queryset= Project.objects.all()
    #para cualquier servidor pueder ver mi servido
    permission_classes =[permissions.AllowAny()]