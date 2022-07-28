from django.contrib import admin
from account.models import Account, Transaction, JournalEntry

class AccountAdmin(admin.ModelAdmin):
    list_filter = ["type"]
    ordering = ["full_code"]
    list_display = ["name","parent","type","code","full_code"]
    search_fields = ["name","code"]


admin.site.register(Account,AccountAdmin)
admin.site.register(Transaction)
admin.site.register(JournalEntry)
