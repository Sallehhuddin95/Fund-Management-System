import pytest
from myapp.models import InvestmentFund

@pytest.mark.django_db
def test_create_fund():
    fund = InvestmentFund.objects.create(
        name="Test Fund",
        manager_name="Test Manager",
        description="Test Description",
        net_asset_value=1000000.00,
        creation_date="2023-08-26",
        performance=8.5
    )
    assert InvestmentFund.objects.count() == 1