from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from transaction import views
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer

class TestTransactionApi(APITestCase):

    def setUp(self):
        self.one = Transaction.objects.create(sender='9999999999', receiver='8888888888@upi', amount=100)
        self.two = Transaction.objects.create(sender='9999999998', receiver='8888888889@upi', amount=100)

    def test_create_transaction(self):
        sample_payload = { "sender": "1234967824", "receiver": "1234967824@upi", "amount": 1423.0 }
        response =self.client.post(reverse('create_a_tranaction'), sample_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_transaction(self):
        response =self.client.get(reverse('create_a_tranaction'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_each_transaction_details(self):
        response =self.client.get(reverse('get_each_transcation_details', kwargs={'pk': self.one.pk}))
        tone = Transaction.objects.get(pk=self.one.pk)
        serializer = TransactionSerializer(tone)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
