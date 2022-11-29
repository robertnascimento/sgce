from django import forms
from .models import Fornecedor,TipoProduto

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome','cnpj','telefone','codigoPostal','emailFornecedor','fotoFornecedor']

class TipoProdutoForm(forms.ModelForm):
    class Meta:
        model = TipoProduto
        fields = ['nome']