from django.db import models

class CarModel(models.Model):
    # Campos del modelo
    marca = models.CharField(max_length=20, default="Ford")
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, default="Particular")
    precio = models.DecimalField(max_digits=10, decimal_places=2)  
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def condicion_precio(self):
        if self.precio < 10000:
            return "Bajo"
        elif 10000 <= self.precio <= 30000:
            return "Medio"
        else:
            return "Alto"

    class Meta:
                permissions = (
                ("es_miembro_1", "Es miembro con prioridad 1"),
                ("development", "Puede desarrollar"),       
                ("scrum_master", "Es Scrum Master"),       
                ("product_owner", "Es Product Owner"), 
                ("visualizar_catalogo", "Puede visualizar Catálogo de Vehículos"),
                ("add", "Can add vehiculo model"),
                )
    def __str__(self):
        return f"{self.marca} {self.modelo}"
