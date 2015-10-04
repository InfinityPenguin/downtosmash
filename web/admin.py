from django.contrib import admin
from .models import User, Event

class EventInline(admin.TabularInline):
	model = Event
	extra = 0

class UserAdmin(admin.ModelAdmin):
	fields = ['name_last', 'name_first', 'gamer_tag']
	list_display = ('name_last', 'name_first', 'gamer_tag')
	inlines = [EventInline]

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Event)
