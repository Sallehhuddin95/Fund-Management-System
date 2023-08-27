from django.urls import path
from ..views import fund_views as views



urlpatterns = [
    path('', views.fund_list, name="fund-list"),
    path('create/', views.fund_create, name="fund-create"),
]