from rest_framework.test import APIClient
from django.conf import settings
from django.urls import reverse

def test_list_all_funds():
    client = APIClient()
    response = client.get(reverse('fund-list'))
    assert response.status_code == 200

def test_get_specific_fund():
    client = APIClient()
    response = client.get(reverse('get-fund', kwargs={'pk': 1}))
    assert response.status_code == 200

def test_delete_specific_fund():
    client = APIClient()
    response = client.delete(reverse('fund-delete', kwargs={'pk': 1}))
    assert response.status_code == 204

def test_update_specific_fund():
    client = APIClient()
    response = client.put(reverse('fund-update', kwargs={'pk': 1}), {'name': 'test'})
    assert response.status_code == 200