from django.urls import path
from transaction import views

urlpatterns = [
    path('transaction/', views.transaction_list),
    path('transaction/<int:pk>/', views.transaction_detail),
]