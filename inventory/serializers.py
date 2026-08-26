from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the Item model, exposing all fields.
    """

    class Meta:
        model = Item
        fields = "__all__"
