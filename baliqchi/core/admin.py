from django.contrib import admin

from core.models import Target, Incident

# Register your models here.
admin.site.site_header = "Baliqchi Admin"
admin.site.register(Target)
admin.site.register(Incident)