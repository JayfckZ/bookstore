from rest_framework import serializers

from product.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = ["title", "slug", "description", "active"]
