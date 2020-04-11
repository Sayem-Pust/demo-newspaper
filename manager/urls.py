from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^panel/manager/list/$', views.manager_list, name='manager_list'),
    url(r'^panel/manager/del/(?P<pk>\d+)/$', views.manager_del, name='manager_del'),
    url(r'^panel/manager/group/$', views.manager_group, name='manager_group'),
    url(r'^panel/manager/group/add/$', views.manager_group_add, name='manager_group_add'),
    url(r'^panel/manager/group/del/(?P<name>.*)/$', views.manager_group_del, name='manager_group_del'),

]
