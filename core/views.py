from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from .models import Fornecedor, TipoProduto , Produto, Usuario
from .forms import FornecedorForm, TipoProdutoForm , ProdutoForm

@login_required
def perfil(request):
    return render(request,'perfil.html')
"""
FORNECEDORES
"""
@login_required
def fornecedor_lista(request):
    fornec = Fornecedor.objects.all()
    contexto = {
        'list_fornecedor': fornec
    }
    return render(request,'fornecedor_lista.html',contexto)

@login_required
@permission_required('core.CD','core.RU')
def fornecedor_cadastro(request):
    form = FornecedorForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')

    contexto = {
        'form': form
    }

    return render(request,'fornecedorcad.html',contexto)

@login_required
@permission_required('core.RU')
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

@login_required
@permission_required('core.CD','core.RU')
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
    return render(request,'tipoprodutolista.html',contexto)

@login_required
@permission_required('core.CD','core.RU')
def tipoProduto_Cadastro(request):
    form = TipoProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_tipoProduto')

    contexto = {
        'form' : form
    }

    return render(request,'tipoprodutocad.html',contexto)

@login_required
@permission_required('core.RU')
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

@login_required
@permission_required('core.CD','core.RU')
def tipoProduto_Remover(request,id):
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
    return render(request,'produto_lista.html',contexto)

@login_required
@permission_required('core.CD','core.RU')
def produto_cadastro(request):
    form = ProdutoForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_produto')

    contexto = {
        'form': form
    }
    return render(request,'produto_cad.html',contexto)

@login_required
@permission_required('core.RU')
def produto_edit(request,id):
    prd = Produto.objects.get(pk=id)

    form = ProdutoForm(request.POST or None,request.FILES or None,instance=prd)
    if form.is_valid():
        form.save()
        return redirect('list_produto')

    contexto = {
        'form': form
    }
    return render(request,'produto_edit.html',contexto)

@login_required
@permission_required('core.CD','core.RU')
def produto_remover(request,id):
    prd = Produto.objects.get(pk=id)
    prd.delete()
    return redirect('list_produto')










def cadastro_manual(request):
    user = Usuario.objects.create_user(
        username='adsaasas',
        email='admiaaa@gmail.com',
        cpf='13192504404',
        nome='adminaaaro',
        password='123456',
        idade=35,
        is_superuser=False
    )
    
    permission1 = Permission.objects.get(codename='CD')
    permission2 = Permission.objects.get(codename='RU')
    user.user_permissions.add(permission1,permission2)

    user.save()
    return redirect('home')