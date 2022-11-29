from django import forms
from .models import Fornecedor,TipoProduto,Produto

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome','cnpj','telefone','codigoPostal','emailFornecedor','fotoFornecedor']

class TipoProdutoForm(forms.ModelForm):
    class Meta:
        model = TipoProduto
        fields = ['nome']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['modelo','quantidade','fornecedor','equipamento','fotoUm','fotoDois','fotoTres','fotoQuatro','fotoCinco']