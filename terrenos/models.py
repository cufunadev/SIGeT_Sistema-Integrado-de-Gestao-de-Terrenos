from django.db import models

# Create your models here.




class Terreno(models.Model):
    
    LOCALIZACAO_CHOICES = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
        ('industrial', 'Industrial'),
        ('outro', 'Outro'),
    ]

    localizacao = models.CharField(max_length=255)
    metragem = models.DecimalField(max_digits=10, decimal_places=2)
    preco = models.DecimalField(max_digits=15, decimal_places=2)
    finalidade = models.CharField(max_length=50, choices=LOCALIZACAO_CHOICES)
    status = models.CharField(max_length=50, default='disponível')

    def __str__(self):
        return f"Terreno {self.localizacao} ({self.finalidade})"
