from typing import List
from ninja import Router
from account.models import JournalEntry
from account.schema import JournalEntryOut

je_router=Router()

@je_router.get("get_all/",response=List[JournalEntryOut])
def get_all(request):
    jes=JournalEntry.objects.all()
    return 200,jes