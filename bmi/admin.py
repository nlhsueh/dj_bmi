from django.contrib import admin

# Register your models here.
from .models import People, Level


class PeopleAdmin(admin.ModelAdmin):
    list_display = ("pname", "h", "w")


# Register your models here.
admin.site.register(People, PeopleAdmin)
admin.site.register(Level)
