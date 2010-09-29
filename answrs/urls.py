from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import login, logout

urlpatterns = patterns('answrs.views',
    url(r'^$', 'index', name='answrs_index'),
    url(r'^random/$', 'randompage', name='answrs_random'),
    url(r'^ask/$', 'ask', name='answrs_ask'),
    url(r'^ask/(?P<cat_slug>[^\.^/]+)/$', 'ask', name='answrs_ask_cat'),
    url(r'answer/(?P<id>\d+)/', 'answer', name='answrs_answer'),
    url(r'^addcat/$', 'add_cat', name='answrs_add_cat'),
    url(r'^cat/(?P<slug>[^\.^/]+)/$', 'view_cat', name='answrs_view_cat'),
    url(r'^profile/(?P<username>\w+)/', 'profile', name='answrs_profile'),
    url(r'^accounts/profile/', 'profile', name='answrs_self_profile'),
)