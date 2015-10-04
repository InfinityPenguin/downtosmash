from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexView(generic.DetailView):
	model = User
	template_name = 'downtosmash/index.html'

def create_event(request, user_id):
	pass

def down_to_smash(request, user_id, event_id):
	pass

def confirm_attendee(request, host_id, attendee_id):
	pass