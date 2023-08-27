from django.urls import path
from ..views import fund_views as views



urlpatterns = [
    path('', views.fund_list, name="fund-list"),
    path('<str:pk>/', views.fund_get, name="get-fund"),
    path('create/', views.fund_create, name="fund-create"),
    path('update/<str:pk>/', views.fund_update, name="fund-update"),
    path('delete/<str:pk>/', views.fund_delete, name="fund-delete"),
]