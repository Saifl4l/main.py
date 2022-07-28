from typing import List
from ninja import Router
from account.models import Transaction, JournalEntry
from account.schema import TransactionIn

transaction_router=Router()

"""@transaction_router.get("get_all/",response=List[TransactionIn])
def get_all(request):
    transaction=Transaction.objects.all()
    return 200,transaction"""
@transaction_router.post("add_transaction")
def add_transaction(request,transaction_in:TransactionIn):
    t=Transaction.objects.create(
        type=transaction_in.type,
        description=transaction_in.description,
    )
    cje=JournalEntry.objects.create(
        account_id=transaction_in.je.credit_account,
        transaction=t,
        amount=transaction_in.je.amount,
        currency=transaction_in.je.currency
    )
    dje=JournalEntry.objects.create(
        account_id=transaction_in.je.debit_account,
        transaction=t,
        amount=transaction_in.je.amount * -1,
        currency=transaction_in.je.currency
    )
    return 200,None