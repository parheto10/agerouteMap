from django.contrib import admin

from .models import Concessionaire, Ville, Commune, Locale

admin.site.register(Concessionaire)
admin.site.register(Ville)
admin.site.register(Commune)
admin.site.register(Locale)

# Register your models here.
