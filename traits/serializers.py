from datetime import timezone
from rest_framework import serializers

class TraitSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    created_at = serializers.DateTimeField(read_only=True)
    