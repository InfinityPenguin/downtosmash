from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import serializers
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .models import Smasher, Event
from .forms import EventCreateForm, UserCreationForm

# Create your views here.

@login_required
def main(request):
	return render(request, 'web/main.html')

@login_required
def event_view(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	if request.method == 'POST':
		form = EventCreateForm(request.POST, instance=event)
		if form.is_valid():
			form.save()
			message = 'Event updated successfully'
			return render(request, 'web/event_view.html', {'message': message})
	form = EventCreateForm(instance=event)
	return render(request, 'web/event_view.html', {'event': event, 'form': form})

@login_required
def attendees(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	attendee_list = Smasher.objects.all().filter(events__id=event_id)
	print(str(attendee_list))
	return render(request, 'web/attendees.html', {'attendees': attendee_list, 'event': event})

@login_required
def event_details(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	form = EventCreateForm(instance=event)
	return render(request, 'web/event_details.html', {'event': event, 'form': form})

@login_required
def my_events(request):
	events = Event.objects.all().filter(host=request.user)
	return render(request, 'web/my_events.html', {'events': events})

@login_required
def menu(request):
	return render(request, 'web/menu.html')

def user_login(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			form = AuthenticationForm(None, request.POST)
			nextpage = request.GET.get('next')
			if form.is_valid():
				login(request, form.get_user())
				return HttpResponseRedirect(nextpage)
		else:
			form = AuthenticationForm(None)
		return render(request, 'web/login.html', {'form': form, 'next': request.GET.get('next')})
	else:
		return HttpResponseRedirect('/')

def user_logout(request):
	logout(request)
	# Redirect to logout successful
	message = "Logout successful"
	return render(request, 'web/login.html', {'message': message})

@login_required
def event_search(request):
	events = Event.objects.all()
	return render(request, 'web/event_search.html', {'events': events})

@login_required
def event_create(request):
	if request.method == 'POST':
		form = EventCreateForm(request.POST)
		if form.is_valid():
			new_event = form.save(commit=False)
			new_event.host = request.user
			new_event.save()
			message = 'Event created successfully'
			return render(request, 'web/event_create.html', {'message': message})
	else:
		form = EventCreateForm(initial={'start_time': timezone.now(), 'start_date': timezone.now()})
	return render(request, 'web/event_create.html', {'form': form})

def new_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')
	else:
		form = UserCreationForm()
	return render(request, 'web/new_user.html', {'form': form})

class IndexView(generic.DetailView):
	model = Smasher
	template_name = 'downtosmash/index.html'

def create_event(request, user_id):
	pass

def down_to_smash(request, user_id, event_id):
	pass

def confirm_attendee(request, host_id, attendee_id):
	pass
