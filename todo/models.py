# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
	nombre = models.CharField(max_length=50)
	apellido_pat = models.CharField(max_length=50)
	apellido_mat = models.CharField(max_length=50)
	direccion = models.TextField()
	num_control = models.CharField(max_length=10)
	carrera = models.ForeignKey(Carrera, verbose_name="pertenece")

       		       
