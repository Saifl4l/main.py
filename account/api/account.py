from typing import List

from django.db.models import Sum
from django.shortcuts import get_object_or_404
from ninja import Router
from account.models import Account, JournalEntry
from account.schema import AccountOut, FourOfourOut

account_roter = Router()

@account_roter.get("/list_all",response=List[AccountOut])
def get_all(request):
    accounts=Account.objects.all()
    return accounts

@account_roter.get("/get_one/{account_id}/",response={
    200:AccountOut,
    404:FourOfourOut
})
def get_all(request,account_id:int):
    try:
        accounts = Account.objects.get(id=account_id)
        return accounts
    except Account.DoesNotExist:
        return 404, {'detail': f'Account with id {account_id} dose not  except'}

@account_roter.get('account-balance/{account_id}')
def get_account_balance(request,account_id:int):
    account=get_object_or_404(Account,id=account_id)
    balance=account.joumi_entries.values('currency').annotate(sum=Sum('amount')).order_by()
    print(balance)
    return 200,{'account': account.name, 'balance': [b for b in balance] }