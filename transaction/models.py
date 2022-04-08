from django.db import models


class Transaction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.IntegerField()
    receiver = models.TextField()
    amount = models.FloatField()
    status = models.CharField(max_length=100, default='Success Transaction')

    def __str__(self):
        return "%s %s" %(self.id, self.status)

