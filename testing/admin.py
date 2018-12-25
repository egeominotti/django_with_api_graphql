from django.contrib import admin
from testing.models import Utente,Post

class UtenteAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Utente,UtenteAdmin)
admin.site.register(Post,PostAdmin)