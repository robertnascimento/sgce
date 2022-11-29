from django.shortcuts import render,redirect
from .models import Fornecedor, TipoProduto
from .forms import FornecedorForm, TipoProdutoForm

"""
FORNECEDORES
"""
def fornecedor_lista(request):
    fornec = Fornecedor.objects.all()
    contexto = {
        'lista_fornecedores': fornec
    }
    return render(request,'fornecedor_lista.html',contexto)

def fornecedor_cadastro(request):
    form = FornecedorForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_fornecedores')

    contexto = {
        'form': form
    }

    return render(request,'fornecedorcad.html',contexto)

def fornecedorEdit(request,id):
    frnc = Fornecedor.objects.get(pk=id)
    
    form = FornecedorForm(request.POST or None,request.FILES or None, instance=frnc)
    if form.is_valid():
        form.save()
        return redirect('lista_fornecedores')
    
    contexto = {
        'form': form
    }

    return render(request, 'fornecedor_edit.html', contexto)

def fornecedor_remover(request, id):
    frnc = Fornecedor.objects.get(pk=id)
    frnc.delete()
    return redirect('lista_fornecedores')

