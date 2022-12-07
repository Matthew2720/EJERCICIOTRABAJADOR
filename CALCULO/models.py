from django.db import models

# Create your models here.
class Trabajador(models.Model):
    Nombre = models.CharField(max_length=20, null=False,blank=False)
    Cargo = models.CharField(max_length=8,null=False)
    Dias_Trabajados= models.BigIntegerField(null=False)
    Total_Salario = models.BigIntegerField(null=True)
    Mes_Pagado = models.CharField(max_length=15)

    def __str__(self):
        return self.Nombre

    def save(self, *args, **kwargs):
        existe = Trabajador.objects.filter(Nombre = self.Nombre, Cargo = self.Cargo, Mes_Pagado = self.Mes_Pagado, Dias_Trabajados = self.Dias_Trabajados)
        if not existe:
            if self.Cargo == 'Gerente':
                valorDia = 12000
            elif self.Cargo == 'Asesor':
                valorDia = 9000
            else:
                valorDia = 8000
            self.Total_Salario = self.Dias_Trabajados * valorDia
            super(Trabajador, self).save(*args, **kwargs)
        else:
            return 