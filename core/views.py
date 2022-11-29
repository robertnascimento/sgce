from django.shortcuts import render,redirect
from .models import Fornecedor, TipoProduto , Produto
from .forms import FornecedorForm, TipoProdutoForm , ProdutoForm

"""
FORNECEDORES
"""
def fornecedor_lista(request):
    fornec = Fornecedor.objects.all()
    contexto = {
        'list_fornecedor': fornec
    }
    return render(request,'fornecedor_lista.html',contexto)

def fornecedor_cadastro(request):
    form = FornecedorForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')

    contexto = {
        'form': form
    }

    return render(request,'fornecedorcad.html',contexto)

def fornecedor_Edit(request,id):
    frnc = Fornecedor.objects.get(pk=id)
    
    form = FornecedorForm(request.POST or None,request.FILES or None, instance=frnc)
    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')
    
    contexto = {
        'form': form
    }

    return render(request, 'fornecedor_edit.html', contexto)

def fornecedor_remover(request, id):
    frnc = Fornecedor.objects.get(pk=id)
    frnc.delete()
    return redirect('list_fornecedores')






"""
TIPO PRODUTOS
"""

def tipoProduto_Lista(request):
    tpProd = TipoProduto.objects.all()
    contexto = {
        'list_tipoProduto': tpProd
    }
    return render(request,'tipoprodutolista.html',contexto)

def tipoProduto_Cadastro(request):
    form = TipoProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_tipoProduto')

    contexto = {
        'form' : form
    }

    return render(request,'tipoprodutocad.html',contexto)

def tipoProduto_Edit(request,id):
    tprd = TipoProduto.objects.get(pk=id)

    form = TipoProdutoForm(request.POST or None,instance= tprd)
    if form.is_valid():
        form.save()
        return redirect('list_tipoProduto')

    contexto = {
        'form' : form
    }

    return render(request,'tipoprodutoedit.html',contexto)

def tipoProduto_Remover(request,id):
    tprd = TipoProduto.objects.get(pk=id)
    tprd.delete()
    return redirect('list_tipoProduto')



"""
PRODUTOS
"""

def produto_lista(request):
    prod = Produto.objects.all()
    contexto = {
        'list_produto': prod
    }
    return render(request,'produto_lista.html',contexto)

def produto_cadastro(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_produto')

    contexto = {
        'form': form
    }
    return render(request,'produto_cad.html',contexto)

def produto_edit(request,id):
    prd = Produto.objects.get(pk=id)

    form = ProdutoForm(request.POST or None,instance=prd)
    if form.is_valid():
        form.save()
        return redirect('list_produto')

    contexto = {
        'form': form
    }
    return render(request,'produto_edit.html',contexto)

def produto_remover(request,id):
    prd = Produto.objects.get(pk=id)
    prd.delete()
    return redirect('list_produto')