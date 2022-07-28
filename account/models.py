from django.db import models



class Account(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, )
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=255,choices=(
    ("ASSETS", "ASSETS"),
    ("LIABILTIES", "LIABILTIES"),
    ("INCOME", "INCOME"),
    ("EXPENSES", "EXPENSES")
    ))
    code = models.CharField(max_length=25)
    full_code = models.CharField(max_length=25)
    extra=models.JSONField(default=dict,null=True,blank=True)
    def __str__(self):
        return f'{self.code}-{self.name}'
class Transaction(models.Model):
    type = models.CharField(max_length=25, choices=[
        ("invoice", "invoice"),
        ("income", "income"),
        ("expense", "expense"),
        ("bill", "bill"),
    ])
    description = models.CharField(max_length=255)


class JournalEntry (models.Model):
    class Meta:
        verbose_name_plural="JoumiEntries"
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="joumi_entries")
    transaction= models.ForeignKey(Transaction, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=25, decimal_places=4)
    currency = models.CharField(max_length=25, choices=[
        ("USD", "USD"),
        ("IQD", "IQD"),
    ])
    def __str__(self):
        return f'{self.account} - {self.amount} - {self.currency}'

