from django.contrib import admin
from .models import Getitdone

# modifying the admin panel to display a field which we cannot edit
class GetitdoneAdmin(admin.ModelAdmin):
    readonly_fields=('created',)

admin.site.register(Getitdone,GetitdoneAdmin)

