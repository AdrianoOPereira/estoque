from django.db import models

class Estoque(models.Model):
    Qtde = models.IntegerField(null=False, blank=False)
    Codigo = models.CharField(max_length=30, null=False, blank=False)
    Descricao = models.CharField(max_length=100, null=False, blank=False)
    Categoria = models.CharField(max_length=30)
    Ncm = models.CharField(max_length=10)
    Qtde_Recebida = models.IntegerField(null=False, blank=False)
    Pç_Utilizadas = models.IntegerField(null=False, blank=False)
    Estoque_Inicial = models.IntegerField(null=False, blank=False)
    Estoque_Corrigido = models.IntegerField(null=False, blank=False)
    Unitario = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    Total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"{self.Qtde} - {self.Codigo} - {self.Descricao} - {self.Unitario} - {self.Total}"
