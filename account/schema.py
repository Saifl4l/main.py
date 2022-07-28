from decimal import Decimal
from typing import List

from ninja import Schema


class AccountOut(Schema):
    id:int
    parent:'AccountOut'=None
    name:str
    type:str
    code:str
    full_code:str


class FourOfourOut(Schema):
    detail:str

class JournalEntry(Schema):
    account:int
    transaction:int
    amount:float
    currency:str

class JournalEntryOut(JournalEntry):
    id:int

class JournalEntryIn(JournalEntry):
    pass

class JournalEntryInTransactionIn(Schema):
    credit_account:int
    debit_account:int
    amount:float
    currency:str


class TransactionIn(Schema):
    type:str
    description:str
    je:JournalEntryInTransactionIn
AccountOut.update_forward_refs()