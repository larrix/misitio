from django.conf.urls import url

from . import views

urlpatterns = [
    # Ejemplo: /encuestas/
    url(r'^$', views.index, name='index'),
    # ex: /encuestas/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /encuestas/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /encuestas/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]