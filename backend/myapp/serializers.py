from rest_framework import serializers
from .models import InvestmentFund


class InvestmentFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentFund
        fields = '__all__'

    # validate performance field to be % value between -100% to positive infinity
    def validate_performance(self, value):
        if value < -100:
            raise serializers.ValidationError("Performance cannot be less than -100%")
        return value
    
    # validate net_asset_value field to be positive value
    def validate_net_asset_value(self, value):
        if value < 0:
            raise serializers.ValidationError("Net Asset Value cannot be negative")
        return value


