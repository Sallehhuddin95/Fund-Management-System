from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import InvestmentFund
from ..serializers import InvestmentFundSerializer

# Create your views here.
# get all funds
@api_view(['GET'])
def fund_list(request):
    try:
        funds = InvestmentFund.objects.all()
        serializer = InvestmentFundSerializer(funds, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    


# get specific fund by id
@api_view(['GET'])
def fund_get(request, pk):
        
    try:
        fund = InvestmentFund.objects.get(id=pk)
        serializer = InvestmentFundSerializer(fund, many=False)
        return Response(serializer.data)
    except InvestmentFund.DoesNotExist:
        return Response({"error": "Fund not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# add new fund
@api_view(['POST'])
def fund_create(request):
    try:
        serializer = InvestmentFundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# update fund
@api_view(['PUT'])
def fund_update(request, pk):
    try:
        fund = InvestmentFund.objects.get(id=pk)
        serializer = InvestmentFundSerializer(instance=fund, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except InvestmentFund.DoesNotExist:
        return Response({"error": "Fund not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# delete fund
@api_view(['DELETE'])
def fund_delete(request, pk):
    try:
        fund = InvestmentFund.objects.get(id=pk)
        fund.delete()
        return Response("Fund deleted successfully", status=status.HTTP_204_NO_CONTENT)
    except InvestmentFund.DoesNotExist:
        return Response({"error": "Fund not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)