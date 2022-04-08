from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from datetime import datetime, timedelta

@csrf_exempt
def transaction_list(request):
    """
    List all code transactions, or create a new transaction.
    """
    if request.method == 'GET':
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            time_threshold = datetime.utcnow() - timedelta(minutes=2)
            count = (Transaction.objects.filter(timestamp__gt=time_threshold) & Transaction.objects.filter(amount= data['amount'])).count()
            sender_no = int(data['sender'])
            reciever_no = int(data['receiver'][:10])
            if (sender_no == reciever_no) or (count > 10):
                data['status'] = 'Unsuccessful Transaction'
                serializer = TransactionSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                return JsonResponse({'message':'terrorist spotted'}, status=201)
            serializer = TransactionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse({'message':'not a terrorist'}, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def transaction_detail(request, pk):
    """
    Retrieve a code transaction.
    """
    try:
        transaction = Transaction.objects.get(pk=pk)
    except Transaction.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return JsonResponse(serializer.data)