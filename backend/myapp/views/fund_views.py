from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import InvestmentFund
from ..serializers import InvestmentFundSerializer

# Create your views here.
# get all funds
@api_view(['GET'])
def fund_list(request):
    funds = InvestmentFund.objects.all()
    serializer = InvestmentFundSerializer(funds, many=True)
    return Response(serializer.data)


# add new fund
@api_view(['POST'])
def fund_create(request):
    serializer = InvestmentFundSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)