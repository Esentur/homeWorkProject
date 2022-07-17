from rest_framework import serializers

from apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    # Валидация name.title
    def validate(self, attrs):
        print(attrs)
        title = attrs.get('name')
        title = title.title()
        attrs['name'] = title
        return attrs

