from django.forms import *
from .models import *

class TrabajadorForm(ModelForm):
    class Meta:
        model = Trabajador
        fields = ('Nombre','Cargo','Dias_Trabajados','Mes_Pagado')
        CHOICES = (('Gerente', 'Gerente'),('Asesor', 'Asesor'),('Vendedor', 'Vendedor'))
        CHOICESMONTH = (('Enero','Enero'),('Febrero','Febrero'),('Marzo','Marzo'),('Abril','Abril'),('Mayo','Mayo'),('Junio','Junio'),
        ('Julio','Julio'),('Agosto','Agosto'),('Septiembre','Septiembre'),('Octubre','Octubre'),('Noviembre','Noviembre'),('Diciembre','Diciembre'))
        widgets = {
            'Nombre':TextInput(attrs={'class':'form-control'}),
            'Cargo':Select(attrs={'class':'form-control'},choices= CHOICES ),
            'Dias_Trabajados':NumberInput(attrs={'class':'form-control'}),
            'Mes_Pagado' : Select(attrs={'class':'form-control'},choices= CHOICESMONTH ),
        }