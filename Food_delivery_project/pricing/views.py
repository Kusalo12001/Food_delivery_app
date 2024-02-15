from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from pricing.models import Pricing
from pricing.serializers import PricingSerializer

class DeliveryCostView(APIView):
    def post(self, request):
        data = request.data
        zone = data.get('zone')
        organization_id = data.get('organization_id')
        total_distance = data.get('total_distance')
        item_type = data.get('item_type')

        try:
            pricing = Pricing.objects.get(organization_id=organization_id, zone=zone)
        except Pricing.DoesNotExist:
            return Response({"error": "Pricing not found for the given organization and zone"}, status=status.HTTP_404_NOT_FOUND)

        base_distance = pricing.base_distance_in_km
        km_price = pricing.km_price
        fix_price = pricing.fix_price

        if item_type == 'perishable':
            total_price = fix_price + (max(total_distance - base_distance, 0) * km_price)
        else:
            total_price = fix_price + (max(total_distance - base_distance, 0) * km_price)

        return Response({"total_price": total_price})
