from django.urls import path
from pricing.views import DeliveryCostView

urlpatterns = [
    path('calculate-delivery-cost/', DeliveryCostView.as_view(), name='calculate_delivery_cost'),
]
