from django import forms


class CreateDetailRouteForm(forms.Form):
    rota = forms.IntegerField(label="ID da rota", required=False)
    codigo = forms.CharField(max_length=50, required=True, label="Codigo da rota")
    status = forms.CharField(max_length=2, required=True, label="Status", empty_value="A")
    descricao = forms.CharField(max_length=150, required=True, label="Descrição da rota")
    fornecedor = forms.IntegerField(required=True, label="ID fornecedor")
    api = forms.IntegerField(required=False, label="API vinculada")


class SearchRouteForm(forms.Form):
    search = forms.CharField(max_length=50, required=True)
