from django.db import models
from SnB.entitydb.models import Entity

class Invoice(models.Model):
    def __unicode__(self):
        return self.sender.getFullName() + " - " + self.date.__str__()

    sender = models.ForeignKey('entitydb.Entity', related_name='sender')
    recipient = models.ForeignKey('entitydb.Entity', related_name='recipient')
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField(upload_to='invoices/%Y/%m/')

class Transaction(models.Model):
    def __unicode__(self):
        return self.payer.getFullName() + "->" + self.payee.getFullName() + " - " + self.date.__str__()

    TYPE_CHOICES = (
        ('cash', 'Cash'),
        ('check', 'Check'),
        ('charge', 'Charge')
    )
    payer = models.ForeignKey('entitydb.Entity', related_name='payer')
    payee = models.ForeignKey('entitydb.Entity', related_name='payee')
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    meta = models.CharField(max_length=128, help_text="Check number or other distinquishing information regarding this transaction")
    invoice = models.ForeignKey('Invoice', null=True, blank=True)

