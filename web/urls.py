from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^main/$', views.main, name='main'),
	url(r'^event_search/$', views.event_search, name='event_search'),
	url(r'^event_create/$', views.event_create, name='event_create'),
	url(r'^menu/$', views.menu, name='menu'),
	url(r'^login/$', views.login, name='login'),
	url(r'^new_user/$', views.new_user, name='new_user'),
	url(r'^event_window/$', views.event_window, name='event_window'),
	url(r'^my_events/$', views.my_events, name='my_events'),
]
