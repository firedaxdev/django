
# Create your views here.
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Entrada, Categoria
#Define tus vistas para Blog

def index(request):
	return render(request, 'index.fdx', {
		'categorias':Categoria.objects.all(),
		'entradas':Entrada.objects.all()

	})

def EntradaDetalles(request, slug):
	meses = {
		1:"Enero",
		2:"Febrero",
		3:"Marzo",
		4:"Abril",
		5:"Mayo",
		6:"Junio",
		7:"Julio",
		8:"Agosto",
		9:"Septiembre",
		10:"Octubre",
		11:"Noviembre",
		12:"Diciembre"
		}
	entrada = get_object_or_404(Entrada, slug=slug)
	dia = entrada.publicado.day
	mes = meses[entrada.publicado.month]
	year = entrada.publicado.year

	return render(request, 'detalle.fdx', locals())

def CategoriaPaginacion(request, slug):
	seleccionada = get_object_or_404(Categoria, slug=slug)
	return render(request, 'categoria.fdx', {
		'categoria':seleccionada,
		'entradas':Entrada.objects.filter(categoria=seleccionada)
	})
