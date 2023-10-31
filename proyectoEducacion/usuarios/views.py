from django.shortcuts import render

from .models import Ciudad, Pais, Provincia
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


from .forms import CiudadForm

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'ciudad_list'

    def get_queryset(self):
        return Ciudad.objects.all()

class CiudadDetalleView(DetailView):
    model = Ciudad
    template_name = 'ciudad_detalle.html'


def create(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = CiudadForm()

    return render(request, 'create.html', {'form': form})

def edit(request, pk, template_name='edit.html'):
    ciudad = get_object_or_404(Ciudad, pk=pk)
    form = CiudadForm(request.POST or None, instance = ciudad)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})

def delete(request, pk, template_name='confirm_delete.html'):
    ciudad = get_object_or_404(Ciudad, pk=pk)
    if request.method=='POST':
        ciudad.delete()
        return redirect('index')
    return render(request, template_name, {'object': ciudad})
