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
from core.views import fornecedor_lista,fornecedorEdit,fornecedor_cadastro,fornecedor_remover

urlpatterns = [
    path('fornecedoresEdit/<int:id>',fornecedorEdit,name='edit_fornecedor'),
    path('fornecedoresCad/',fornecedor_cadastro,name='cad_fornecedores'),
    path('fornecedoresList/',fornecedor_lista,name='lista_fornecedores'),
    path('fornecedoresDelete/<int:id>',fornecedor_remover,name='fornecedore_remover'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

