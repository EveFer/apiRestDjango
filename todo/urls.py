from django.conf.urls import url
from todo import views

urlpatterns = [
    url(r'^alumnos/$', views.alumno_list),
    url(r'^alumno/(?P<pk>[0-9]+)/$', views.alumno_detail),
    url(r'^carreras/$', views.carrera_list),
    url(r'^carrera/(?P<pk>[0-9]+)/$', views.carrera_detail),
]