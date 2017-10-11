from decimal import Decimal

from django.db import models


TX_FAILED = -5
TX_RECURRING_CANCELLED = -4
TX_INSUFFICIENT_FUNDS = -3
TX_TIME_OUT = -2
TX_REJECTED = -1
TX_ACCEPTED = 0
TX_PENDING = 1
TX_AUTHORIZED = 2
TX_PAID = 3
TX_VOIDED = 4

TRANSACTION_STATUS_CHOICES = (
    (TX_FAILED, 'Failed'),
    (TX_RECURRING_CANCELLED, 'Recurring Cancelled'),
    (TX_INSUFFICIENT_FUNDS, 'Insufficient Funds'),
    (TX_TIME_OUT, 'Timed Out'),
    (TX_REJECTED, 'Rejected'),
    (TX_ACCEPTED, 'Accepted'),
    (TX_PENDING, 'Pending'),
    (TX_AUTHORIZED, 'Authorized'),
    (TX_PAID, 'Paid'),
    (TX_VOIDED, 'Voided')
)


class MBillsTransaction(models.Model):
    transaction_id = models.CharField(max_length=255)

    amount = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0'))
    currency = models.CharField(max_length=255, default='EUR')
    purpose = models.CharField(max_length=255)

    payment_reference = models.CharField(max_length=255, null=True, blank=True)
    capture = models.BooleanField(default=True)

    order_id = models.CharField(max_length=255, null=True, blank=True)
    channel_id = models.CharField(max_length=255, null=True, blank=True)

    payment_token_number = models.CharField(max_length=255)

    status = models.IntegerField(choices=TRANSACTION_STATUS_CHOICES, default=TX_ACCEPTED)

    transaction_type = models.CharField(max_length=255, default='T')
    settled_amount = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0'))
    fees = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0'))

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "MBills Transaction"

    def __str__(self):
        return self.transaction_id
