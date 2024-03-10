from django.db import models

class Estoque(models.Model):
    Qtde = models.CharField(max_length=30,null=False,blank=False)
    Codigo = models.CharField(max_length=30,null=False,blank=False)
    Descricao = models.CharField(max_length=100,null=False, blank=False )
    Unitario = models.CharField(max_length=30,null=False,blank=False)
    Total = models.CharField(max_length=30,null=False,blank=False)
    
    def __str__(self):
        return f"{self.Qtde} - {self.Codigo} - {self.Descricao} - {self.Unitario} - {self.Total}"
    