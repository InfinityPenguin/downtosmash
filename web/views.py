from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import serializers
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.contrib.auth import authenticate, login, logout

from .models import Smasher, Event, Attendee
from .forms import EventForm, UserCreationForm, AttendeeForm, HostAttendeeForm

# Create your views here.

@login_required
def main(request):
	return render(request, 'web/main.html')

@login_required
def event_view(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	if request.method == 'POST':
		form = EventForm(request.POST, instance=event)
		if form.is_valid():
			form.save()
			message = 'Event updated successfully'
			return render(request, 'web/event_view.html', {'message': message})
	form = EventForm(instance=event)
	return render(request, 'web/event_view.html', {'event': event, 'form': form}) 

@login_required
def attendees(request, event_id):
	message = ""
	event = get_object_or_404(Event, pk=event_id)
	attendee_list = Attendee.objects.filter(event=event)
	AttendeeFormSet = modelformset_factory(Attendee, form=HostAttendeeForm, extra=0)
	if request.method == 'POST':
		formset = AttendeeFormSet(request.POST, request.FILES)
		if formset.is_valid():
			message = "Update successful"
			formset.save()
	formset = AttendeeFormSet(queryset=attendee_list)
	return render(request, 'web/attendees.html', {'formset': formset, 'event': event, 'message': message})

@login_required
def approve_attendee(request, attendee_id):
	attendee = get_object_or_404(Attendee, pk=attendee_id)
	attendee.status = 'AP'

@login_required
def unconfirm_attendee(request, attendee_id):
	attendee = get_object_or_404(Attendee, pk=attendee_id)
	attendee.status = 'IN'

@login_required
def event_details(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	event_form = EventForm(instance=event)
	attendee = get_attendee(event, request.user)
	if request.method == 'POST':
		form = AttendeeForm(request.POST, instance=attendee)
		if form.is_valid():
			form.save()
			message = 'Status updated successfully'
			return render(request, 'web/event_details.html', {'message': message})
	attendee_form = AttendeeForm(instance=attendee)
	return render(request, 'web/event_details.html', {'event': event, 'form': event_form, 'attendee': attendee, 'attendee_form': attendee_form})

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
				print(str(form.get_user()))
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

def new_user(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				print(request.POST)
				user = authenticate(username=request.POST['email'], password=request.POST['password1'])
				login(request, user)
				return HttpResponseRedirect('')
		else:
			form = UserCreationForm()
		return render(request, 'web/new_user.html', {'form': form})
	else:
		return HttpResponseRedirect('/')

@login_required
def event_search(request):
	events = Event.objects.all()
	return render(request, 'web/event_search.html', {'events': events})

@login_required
def event_create(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			new_event = form.save(commit=False)
			new_event.host = request.user
			new_event.save()
			message = 'Event created successfully'
			return render(request, 'web/event_create.html', {'message': message})
	else:
		form = EventForm(initial={'start_time': timezone.now(), 'start_date': timezone.now()})
	return render(request, 'web/event_create.html', {'form': form})

class IndexView(generic.DetailView):
	model = Smasher
	template_name = 'downtosmash/index.html'

def get_attendee(event, user):
	attendee = Attendee.objects.get(user=user, event=event)
	return attendee

def create_event(request, user_id):
	pass

def down_to_smash(request, user_id, event_id):
	pass

def confirm_attendee(request, host_id, attendee_id):
	pass
