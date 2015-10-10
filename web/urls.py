from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.main, name='main'),
	url(r'^event_search/$', views.event_search, name='event_search'),
	url(r'^event_create/$', views.event_create, name='event_create'),
	url(r'^menu/$', views.menu, name='menu'),
	url(r'^login/$', views.user_login, name='user_login'),
	url(r'^new_user/$', views.new_user, name='new_user'),
	url(r'^event_view/$', views.event_view, name='event_view'),
	url(r'^my_events/$', views.my_events, name='my_events'),
]
