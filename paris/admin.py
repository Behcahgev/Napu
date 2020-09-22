from django.contrib import admin
from .models import Sport, Player, Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
   list_display   = ('name', )
   list_filter    = ('name', )
   ordering       = ('name', )
   search_fields  = ('name', )


admin.site.register(Team, TeamAdmin)
admin.site.register(Sport)
admin.site.register(Player)
