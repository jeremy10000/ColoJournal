from django.contrib import admin
from journal.models import Journal, Page


class JournalAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "shared", "date")


class PageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "journal", "text")


admin.site.register(Journal, JournalAdmin)
admin.site.register(Page, PageAdmin)
