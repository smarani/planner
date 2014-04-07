from django.conf.urls import patterns, url

from planner import views

urlpatterns = patterns('',
     # ex: /polls/
    url(r'^$', views.index, name='index'),
    
    url(r'^signedin/$', views.name, name='name'), 
	url(r'^(?P<major_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<major_id>\d+)/results/$', views.results, name='results'),
	url(r'^(?P<major_id>\d+)/vote/$', views.vote, name='vote'),

)
