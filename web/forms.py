from django.forms import ModelForm, SplitDateTimeWidget
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone
from web.models import Smasher, Event

import html5.forms.widgets as html5_widgets

class EventCreateForm(ModelForm):
	class Meta:
		model = Event
		fields = ['start_time',
					'start_date',
					'capacity',
					'location',
					'notes',
					]
		widgets = {'start_time': html5_widgets.TimeInput,
					'start_date': html5_widgets.DateInput,
					}
