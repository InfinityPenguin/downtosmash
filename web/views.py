from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Smasher, Event
from .forms import EventCreateForm

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

@login_required
def event_create(request):
	if request.method == 'POST':
		form = EventCreateForm(request.user)
		if form.is_valid():
			form.save()
			message = 'Event created successfully'
			return render(request, 'web/event_create.html', {'message': message})
	else:
		form = EventCreateForm(initial={'start_time': timezone.now(), 'start_date': timezone.now()})
	return render(request, 'web/event_create.html', {'form': form})

class IndexView(generic.DetailView):
	model = Smasher
	template_name = 'downtosmash/index.html'

def create_event(request, user_id):
	pass

def down_to_smash(request, user_id, event_id):
	pass

def confirm_attendee(request, host_id, attendee_id):
	pass
