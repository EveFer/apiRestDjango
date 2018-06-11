from rest_framework import serializers
from todo.models import Alumno, Carrera

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ('id', 'nombre','clave')

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido_pat', 'apellido_mat', 'direccion', 'num_control', 'carrera')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Alumno.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido_pat = validated_data.get('apellido_pat', instance.code)
        instance.apellido_mat = validated_data.get('apellido_mat', instance.linenos)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.num_control = validated_data.get('num_control', instance.num_control)
        instance.carrera = validated_data.get('carrera', instance.carrera)
        instance.save()
        return instance