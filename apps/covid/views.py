from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.urls import reverse_lazy
from datetime import date, datetime
from apps.covid.models import *

import json
from django.http import JsonResponse


from collections import OrderedDict as SortedDict
def index(request):
	return render(request, 'index.html')
def instalaciones(request):
	return render(request, 'menu/Instalaciones.html')
def servicios(request):
	return render(request, 'menu/Servicios.html')
def contacto(request):
	return render(request, 'menu/Contacto.html')
def graficas(request):
	if(request.user.is_authenticated and (request.user.rol == 0 or request.user.rol == 2)):
		return render(request, 'graficas_covid.html')
	else:
		return redirect('/')	
# Create your views here.
def pruebas_resumen(request):
	porResultado =CuadroMedico.objects.all()
	finalrep ={}
	positivo = 0 
	negativo = 0
	for item in porResultado:
		if item.estado_paciente == 1:		
			positivo = positivo + 1
		if item.estado_paciente == 0:
			negativo = negativo + 1

	finalrep["Pacientes Positivos"]=positivo
	finalrep["Pacientes Negativos"]=negativo

	def listsort(value):
		if isinstance(value,dict):
			new_dict = SortedDict()
			key_list = value.keys()
			key_list=sorted(key_list)
			for key in key_list:
				new_dict[key] = value[key]
			return new_dict
	
	finalrep = listsort(finalrep) 
	return JsonResponse({'pruebas_resumen':finalrep},safe=False)

def pruebas_resumen_genero(request):
	porResultado =CuadroMedico.objects.filter(estado_paciente=1)
	finalrep ={}
	Femenino = 0 
	Masculino = 0
	for item in porResultado:
		if item.paciente.sexo_paciente == 1:		
			Femenino = Femenino + 1
		if item.paciente.sexo_paciente == 0:
			Masculino = Masculino + 1

	finalrep["Femeninos"]=Femenino
	finalrep["Masculinos"]=Masculino

	def listsort(value):
		if isinstance(value,dict):
			new_dict = SortedDict()
			key_list = value.keys()
			key_list=sorted(key_list)
			for key in key_list:
				new_dict[key] = value[key]
			return new_dict
	
	finalrep = listsort(finalrep) 
	return JsonResponse({'pruebas_resumen_genero':finalrep},safe=False)

def pruebas_resumen_genero_sospechosos(request):
	porResultado =CasoSospechoso.objects.all()
	finalrep ={}
	Femenino = 0 
	Masculino = 0
	for item in porResultado:
		if item.sexo_sospechoso == 1:		
			Femenino = Femenino + 1
		if item.sexo_sospechoso == 0:
			Masculino = Masculino + 1

	finalrep["Femeninos"]=Femenino
	finalrep["Masculinos"]=Masculino

	def listsort(value):
		if isinstance(value,dict):
			new_dict = SortedDict()
			key_list = value.keys()
			key_list=sorted(key_list)
			for key in key_list:
				new_dict[key] = value[key]
			return new_dict
	
	finalrep = listsort(finalrep) 
	return JsonResponse({'pruebas_resumen_genero_sospechosos':finalrep},safe=False)

def pruebas_departamento(request):
	porResultado =CuadroMedico.objects.all()
	finalrep ={}
	dep1 = 0
	dep2 = 0
	dep3 = 0
	dep4 = 0
	dep5 = 0
	dep6 = 0
	dep7 = 0
	dep8 = 0
	dep9 = 0
	dep10 = 0
	dep11 = 0
	dep12 = 0
	dep13 = 0
	dep14 = 0

	for item in porResultado:
		if ((item.paciente.localidad.departamento.idDepartamento  == 1) and (item.estado_paciente == 1)):		
			dep1 = dep1 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 2) and (item.estado_paciente == 1)):
			dep2 = dep2 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 3) and (item.estado_paciente == 1)):
			dep3 = dep3 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 4) and (item.estado_paciente == 1)):
			dep4 = dep4 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 5) and (item.estado_paciente == 1)):
			dep5 = dep5 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 6) and (item.estado_paciente == 1)):
			dep6 = dep6 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 7) and (item.estado_paciente == 1)):
			dep7 = dep7 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 8) and (item.estado_paciente == 1)):
			dep8 = dep8 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 9) and (item.estado_paciente == 1)):
			dep9 = dep9 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 10) and (item.estado_paciente == 1)):
			dep10 = dep10 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 11) and (item.estado_paciente == 1)):
			dep11 = dep11 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 12) and (item.estado_paciente == 1)):
			dep12 = dep12 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 13) and (item.estado_paciente == 1)):
			dep13 = dep13 + 1
		if ((item.paciente.localidad.departamento.idDepartamento  == 14) and (item.estado_paciente == 1)):
			dep14 = dep14 + 1

	finalrep["Chalatenango"]=dep1
	finalrep["Cuscatlán"]=dep2
	finalrep["San Salvador"]=dep3
	finalrep["La Libertad"]=dep4
	finalrep["San Vicente"]=dep5
	finalrep["Cabañas"]=dep6
	finalrep["La Paz"]=dep7
	finalrep["Santa Ana"]=dep8
	finalrep["Usulután"]=dep9
	finalrep["San Miguel"]=dep10
	finalrep["Morazán"]=dep11
	finalrep["La Unión"]=dep12
	finalrep["Ahuachapán"]=dep13
	finalrep["Sonsonate"]=dep14

	def listsort(value):
		if isinstance(value,dict):
			new_dict = SortedDict()
			key_list = value.keys()
			key_list=sorted(key_list)
			for key in key_list:
				new_dict[key] = value[key]
			return new_dict
	
	finalrep = listsort(finalrep) 
	return JsonResponse({'pruebas_departamento':finalrep},safe=False)
