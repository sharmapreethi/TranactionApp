from django.urls import path
from transaction import views

urlpatterns = [
    path('transaction/', views.transaction_list, name="create_a_tranaction"),
    path('transaction/<int:pk>/', views.transaction_detail, name="get_each_transcation_details"),
]