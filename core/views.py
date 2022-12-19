from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.shortcuts import redirect, render

from .forms import (FornecedorForm, ProdutoForm, RetiradaForm, TipoProdutoForm,
                    UsuarioCreationForm)
from .models import Fornecedor, Produto, Retiradas, TipoProduto, Usuario


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def perfil(request):
    return render(request, 'perfil.html')


def registro(request):
    form = UsuarioCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
        'form': form
    }

    return render(request, 'registro.html', contexto)


def dados(request, id):
    user = Usuario.objects.get(pk=id)

    form = UserCreationForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('perfil')

    contexto = {
        'form': form
    }
    return render(request, 'registro.html', contexto)


"""
FORNECEDORES
"""


@login_required
def fornecedor_lista(request):
    fornec = Fornecedor.objects.all()
    contexto = {
        'list_fornecedor': fornec
    }
    return render(request, 'fornecedor_lista.html', contexto)


@login_required
def fornecedor_cadastro(request):
    form = FornecedorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')

    contexto = {
        'form': form
    }

    return render(request, 'fornecedorcad.html', contexto)


@login_required
def fornecedor_Edit(request, id):
    frnc = Fornecedor.objects.get(pk=id)

    form = FornecedorForm(request.POST or None,
                          request.FILES or None, instance=frnc)
    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')

    contexto = {
        'form': form
    }

    return render(request, 'fornecedor_edit.html', contexto)


@login_required
def fornecedor_remover(request, id):
    frnc = Fornecedor.objects.get(pk=id)
    frnc.delete()
    return redirect('list_fornecedores')


"""
TIPO PRODUTOS
"""


@login_required
def tipoProduto_Lista(request):
    tpProd = TipoProduto.objects.all()
    contexto = {
        'list_tipoProduto': tpProd
    }
    return render(request, 'tipoprodutolista.html', contexto)


@login_required
def tipoProduto_Cadastro(request):
    form = TipoProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_tipoProduto')

    contexto = {
        'form': form
    }

    return render(request, 'tipoprodutocad.html', contexto)


@login_required
def tipoProduto_Edit(request, id):
    tprd = TipoProduto.objects.get(pk=id)

    form = TipoProdutoForm(request.POST or None, instance=tprd)
    if form.is_valid():
        form.save()
        return redirect('list_tipoProduto')

    contexto = {
        'form': form
    }

    return render(request, 'tipoprodutoedit.html', contexto)


@login_required
def tipoProduto_Remover(request, id):
    tprd = TipoProduto.objects.get(pk=id)
    tprd.delete()
    return redirect('list_tipoProduto')


"""
PRODUTOS
"""


@login_required
def produto_lista(request):
    prod = Produto.objects.all()
    contexto = {
        'list_produto': prod
    }
    return render(request, 'produto_lista.html', contexto)


@login_required
def produto_cadastro(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_produto')

    contexto = {
        'form': form
    }
    return render(request, 'produto_cad.html', contexto)


@login_required
def produto_edit(request, id):
    prd = Produto.objects.get(pk=id)

    form = ProdutoForm(request.POST or None,
                       request.FILES or None, instance=prd)
    if form.is_valid():
        form.save()
        return redirect('list_produto')

    contexto = {
        'form': form
    }
    return render(request, 'produto_edit.html', contexto)


@login_required
def produto_remover(request, id):
    prd = Produto.objects.get(pk=id)
    prd.delete()
    return redirect('list_produto')


def retiradas(request, id):
    prod = Produto.objects.get(pk=id)
    form = RetiradaForm(request.POST or None)

    if form.is_valid():
        qtd = form.cleaned_data['quantidaderet']
        prod.quantidade = (prod.quantidade - qtd)
        form.save()
        prod.save()

        return redirect('list_produto')

    contexto = {
        'form': form
    }

    return render(request, 'retirada.html', contexto)


def retiradasrealizadas(request):
    rtrd = Retiradas.objects.all()
    contexto = {
        'rtrok': rtrd
    }
    return render(request, 'retiradasrealizadas.html', contexto)
