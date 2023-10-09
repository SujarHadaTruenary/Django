from rest_framework import serializers
from .models import todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = todo
        fields = ('id', 'url', 'name', 'done')