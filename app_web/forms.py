from django import forms


class Alta_producto(forms.Form):

    nombre = forms.CharField(max_length=40)
    codigo = forms.IntegerField()

class Alta_cliente(forms.Form):

    nombre = forms.CharField(max_length=40)
    os = forms.IntegerField()
    cod_os = forms.IntegerField()
    fec = forms.DateField()

class Alta_os(forms.Form):

    nombre = forms.CharField(max_length=40)
    cod_os = forms.IntegerField()
    nombre_prod = forms.CharField(max_length=40)
    codigo_prod = forms.IntegerField()
    

