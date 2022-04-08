from rest_framework import serializers
from transaction.models import Transaction


class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)   
    sender = serializers.CharField(required=False, allow_blank=True, max_length=100)
    receiver = serializers.CharField(style={'base_template': 'textarea.html'})
    amount = serializers.FloatField(required=False)
    status = serializers.CharField(required=False)

    def create(self, validated_data):
        """
        Run and return a new `Transaction` instance, given the validated data.
        """
        return Transaction.objects.create(**validated_data)