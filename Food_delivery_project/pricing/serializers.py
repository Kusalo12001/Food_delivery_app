from rest_framework import serializers
from pricing.models import Pricing

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = ['organization', 'item', 'zone', 'base_distance_in_km', 'km_price', 'fix_price']
