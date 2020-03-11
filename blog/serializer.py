from rest_framework import serializers
from .models import posts

class postSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = posts
        fields = ('title', 'body', 'created_at')
