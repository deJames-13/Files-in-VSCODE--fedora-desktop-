from django.db import models
from rest_framework.serializers import ModelSerializer
# Create your models here.

class Data(models.Model):
    data = models.JSONField()
    name = models.CharField(primary_key=True, max_length=255)
    
    def __str__(self) -> str:
        return self.name
    # scores = models.TextField(null=True, blank=True)
    
class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'