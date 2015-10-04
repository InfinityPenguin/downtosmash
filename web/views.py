from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import User, Event

# Create your views here.

def index(request):
	return HttpResponse('Down to smash?')

def main(request):
	return render(request, 'web/main.html')

def event_window(request):
	return render(request, 'web/event_window.html')

def event_details(request):
	return render(request, 'web/event_details.html')

def my_events(request):
	return render(request, 'web/my_events.html')

def menu(request):
	return render(request, 'web/menu.html')

def login(request):
	return render(request, 'web/login.html')

def event_search(request):
	return render(request, 'web/event_search.html')

def event_create(request):
	return render(request, 'web/event_create.html')

class IndexView(generic.DetailView):
	model = User
	template_name = 'downtosmash/index.html'

def create_event(request, user_id):
	pass

def down_to_smash(request, user_id, event_id):
	pass

def confirm_attendee(request, host_id, attendee_id):
	pass
