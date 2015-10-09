from django.contrib import admin
from .models import Smasher, Event

class EventInline(admin.TabularInline):
	model = Event
	extra = 0

class SmasherAdmin(admin.ModelAdmin):
	fields = ['email', 'name_first', 'name_last', 'gamer_tag', 'last_login']
	list_display = ('email', 'name_first', 'name_last', 'gamer_tag')
	inlines = [EventInline]

class EventAdmin(admin.ModelAdmin):
	fields = ['host', 'start_time', 'start_date', 'capacity', 'location', 'notes']
	list_display = ['host', 'start_time', 'start_date', 'capacity', 'location', 'notes']

# Register your models here.
admin.site.register(Smasher, SmasherAdmin)
admin.site.register(Event, EventAdmin)
