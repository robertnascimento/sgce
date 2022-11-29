"""sgce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import fornecedor_lista,fornecedor_Edit,fornecedor_cadastro,fornecedor_remover
from core.views import tipoProduto_Edit,tipoProduto_Cadastro,tipoProduto_Lista,tipoProduto_Remover

urlpatterns = [
    path('fornecedoresEdit/<int:id>',fornecedor_Edit,name='edit_fornecedor'),
    path('fornecedoresCad/',fornecedor_cadastro,name='cad_fornecedores'),
    path('fornecedoresList/',fornecedor_lista,name='lista_fornecedores'),
    path('fornecedoresDelete/<int:id>',fornecedor_remover,name='fornecedore_remover'),

    path('tipoProdutoEdit/<int:id>',tipoProduto_Edit,name='edit_tipoProduto'),
    path('tipoProdutoCad/',tipoProduto_Cadastro,name='cad_tipoProduto'),
    path('tipoProdutoList/',tipoProduto_Lista,name='lista_tipoProduto'),
    path('tipoProdutoDelete/<int:id>',tipoProduto_Remover,name='del_tipoProduto'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

