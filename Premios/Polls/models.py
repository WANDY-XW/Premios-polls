from django.db import models


class Forms(models.Model):
      name = models.CharField(max_length=100)
      date = models.DateTimeField("Publicado")


      def __str__(self) -> str:
            return self.name

class Datos(models.Model):
      correo = models.ForeignKey(Forms,on_delete=models.CASCADE)
      othercorreo = models.CharField(max_length=100)
      numberuser= models.IntegerField(default=0)      

      def __str__(self) -> str:
            return self.correo 

     