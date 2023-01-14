from django.db import models
from django.core.validators import MinLengthValidator

iglesias = (("CATOLICA","Católica"),("ADVENTISTA","Adventista"),("EVANGELICA","Evangélica"),("TESTIGO DE JEHOVA","Testigo de Jehova"),
            ("MORMONA","Mormona"),("UNIVERSAL","Universal"),("CRISTIANA","Cristiana"),("OTRA","Otra"))

sexo = (("M","Masculino"),("F","Femenino"))

grado = (("PRIMARIO","Primario"),("SECUNDARIO","Secundario"),("UNIVERSITARIO","Universitario"))

paises = (("ARGENTINA","Argentina"),("BOLIVIA","Bolivia"),("BRASIL","Brasil"),("COLOMBIA","Colombia"),("COSTA RICA","Costa Rica"),("CUBA","Cuba"),
          ("CHILE","Chile"),("ECUADOR","Ecuador"),("EL SALVADOR","El Salvador"),("GUATEMALA","Guatemala"),
         ( "HONDURAS","Honduras"),("MEXICO","México"),("NICARAGUA","Nicaragua"),("PANAMA","Panamá"),("PARAGUAY","Paraguay"),("PERU","Perú"),
         ("REPUBLICA DOMINICANA","República Dominicana"),("URUGUAY","Uruguay"),("VENEZUELA","Venezuela"))


class datos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    telefono = models.CharField(max_length=10 ,validators=[MinLengthValidator(10)])
    grado_academico = models.CharField(max_length=100, choices=grado)
    ocupacion = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100, choices=sexo, default="Masculino")
    denominacion = models.CharField(max_length=100, choices=iglesias)
    fecha_nacimiento = models.DateField()
    pais = models.CharField(max_length=100, choices=paises, default="REPUBLICA DOMINICANA") 
    provincia = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    email = models.EmailField()
   

