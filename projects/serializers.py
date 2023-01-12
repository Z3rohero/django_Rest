from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        #campos que va ser consultados de mi modelo sql
        fields =('id','title','description','technology','created_at')
        #campos de solo lectura que no se puede modificqar solo pedir
        read_only_fields =('created_at',)

