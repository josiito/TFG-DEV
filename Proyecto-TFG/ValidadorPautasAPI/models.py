from django.db import models

class Documento(models.Model):
    id          = models.IntegerField(primary_key=True)
    descripcion = models.TextField(max_length=200)
    passed      = models.BooleanField(default=False)
    reason      = models.CharField(max_length=300, default="")

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f'Documento {self.id} - {self.descripcion}.\n\t Cumple con las pautas?: {"Sí" if self.passed else "No"} - {self.reason if self.passed else ""}'