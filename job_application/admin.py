from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_filter = ('first_name','last_name','email')
    list_filter = ('date','occupation')
    ordering = ('.first_name')
    readonly_fields = ('occupation')

admin.site.register(Form)