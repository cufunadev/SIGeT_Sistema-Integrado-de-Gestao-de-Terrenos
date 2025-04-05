
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Terreno
from .forms import TerrenoForm

def listar_terrenos(request):
    terrenos = Terreno.objects.all()  # Obtendo todos os terrenos do banco de dados
    return render(request, 'terrenos/listar_terrenos.html', {'terrenos': terrenos})


# Cadastrar Terreno
def cadastrar_terreno(request):
    if request.method == 'POST':
        form = TerrenoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_terrenos')
    else:
        form = TerrenoForm()
    return render(request, 'terrenos/cadastrar_terreno.html', {'form': form})



# Editar Terreno
def editar_terreno(request, pk):
    terreno = get_object_or_404(Terreno, pk=pk)
    if request.method == 'POST':
        form = TerrenoForm(request.POST, instance=terreno)
        if form.is_valid():
            form.save()
            return redirect('listar_terrenos')
    else:
        form = TerrenoForm(instance=terreno)
    return render(request, 'terrenos/editar_terreno.html', {'form': form, 'terreno': terreno})




# Excluir Terreno
def excluir_terreno(request, pk):
    terreno = get_object_or_404(Terreno, pk=pk)
    if request.method == 'POST':
        terreno.delete()
        return redirect('listar_terrenos')
    return render(request, 'terrenos/excluir_terreno.html', {'terreno': terreno})
