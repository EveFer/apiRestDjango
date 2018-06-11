# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from todo.models import Carrera, Alumno

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Alumno)
