from django.contrib import admin
from testing.models import Utente

class UtenteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Utente,UtenteAdmin)