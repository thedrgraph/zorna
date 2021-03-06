from django.conf.urls.defaults import url, patterns

from zorna.calendars import views
from zorna.calendars.feeds import ZornaCalendarICalendar

urlpatterns = patterns('',
                       url(r'^jsonevents/$',
                           views.json_events,
                           name='json_events'),
                       url(r'^calendar/(?P<calendar_id>\d+)/$',
                           views.view_calendar,
                           name='view_calendar'),
                       url(r'^calendar/$',
                           views.view_calendar,
                           name='view_calendar'),
                       url(r'^calendar/edit/$',
                           views.edit_calendar_event,
                           name='edit_calendar_event'),
                       url(r'^calendar/create/$',
                           views.create_calendar_event,
                           name='create_calendar_event'),
                       url(r'^calendar/settings/url/$',
                           views.calendar_settings_shared_url,
                           name='calendar_settings_shared_url'),
                       url(r'^calendar/user/settings/$',
                           views.calendar_user_settings,
                           name='calendar_user_settings'),
                       url(r'^calendar/share/$',
                           views.calendar_share,
                           name='calendar_share'),
                       url(r'^calendar/view/(?P<calendar>\d+)/$',
                           views.add_to_view_calendar,
                           name='add_to_view_calendar'),
                       url(r'^calendar/remove/(?P<calendar>\d+)/$',
                           views.remove_from_view_calendar,
                           name='remove_from_view_calendar'),
                       url(r'^calendar/update/event/dates/$',
                           views.calendar_update_event_dates,
                           name='calendar_update_event_dates'),
                       url(r'^calendar/reset/key/(?P<calendar>\d+)/$',
                           views.calendar_reset_secret_key,
                           name='calendar_reset_secret_key'),
                       url(r'^ical/(.*)/(.*)/$',
                           ZornaCalendarICalendar(),
                           name='calendar_ical'),
                       url(r'^list/$',
                           views.admin_list_calendars,
                           name='admin_list_calendars'),
                       url(r'^add/$',
                           views.admin_add_calendar,
                           name='admin_add_calendar'),
                       url(r'^edit/(?P<resource_calendar>\d+)/$',
                           views.admin_edit_calendar,
                           name='admin_edit_calendar'),
                       url(r'^acl/(?P<resource_calendar>\d+)/$',
                           views.admin_acl_calendar,
                           name='admin_acl_calendar'),
                       )
