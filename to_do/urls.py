from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add', views.add, name='add'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.NoteDelete.as_view(), name='delete'),
]
