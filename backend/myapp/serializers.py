from rest_framework import serializers
from .models import InvestmentFund


class InvestmentFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentFund
        fields = '__all__'


