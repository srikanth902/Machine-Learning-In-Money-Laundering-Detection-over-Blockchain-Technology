from django.db import models
from django.contrib.auth.models import User

class TransactionPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_bank = models.IntegerField()
    to_bank = models.IntegerField()
    amount_received = models.FloatField()
    receiving_currency = models.CharField(max_length=100)
    amount_paid = models.FloatField()
    payment_currency = models.CharField(max_length=100)
    payment_format = models.CharField(max_length=50)

    probability = models.FloatField()
    prediction = models.IntegerField()  # 0 = Not Laundering, 1 = Laundering
    label = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction by {self.user.username} - {self.label}"
