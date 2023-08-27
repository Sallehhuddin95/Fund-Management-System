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


# get specific fund by id
@api_view(['GET'])
def fund_get(request, pk):
    fund = InvestmentFund.objects.get(id=pk)
    serializer = InvestmentFundSerializer(fund, many=False)
    return Response(serializer.data)


# add new fund
@api_view(['POST'])
def fund_create(request):
    serializer = InvestmentFundSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# update fund
@api_view(['PUT'])
def fund_update(request, pk):
    fund = InvestmentFund.objects.get(id=pk)
    serializer = InvestmentFundSerializer(instance=fund, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# delete fund
@api_view(['DELETE'])
def fund_delete(request, pk):
    fund = InvestmentFund.objects.get(id=pk)
    fund.delete()
    return Response("Fund deleted successfully")