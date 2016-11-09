from django.contrib import admin
from User.models import *

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    search_fields = ['name', 'year', 'month']
    list_filter = ['name']

class RSMAdmin(admin.ModelAdmin):
    pass

class RMMAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)

admin.site.register(RSM, RSMAdmin)

admin.site.register(RMM, RMMAdmin)
