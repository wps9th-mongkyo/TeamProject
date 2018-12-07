from rest_framework import serializers

from .models import Eatdeal


class EatdealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eatdeal
        fields = (
            'res_name',
            'deal_name',
            'start_date',
            'end_date',
            'base_price',
            'discount_rate',
            'discount_price',
            'introduce_res',
            'introduce_menu',
            'caution',
            'how_to_use',
            'refund',
            'inquiry',
        )
