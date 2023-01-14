# Generated by Django 4.1.5 on 2023-01-10 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fundacion", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datos",
            name="pais",
            field=models.CharField(
                choices=[
                    ("ARGENTINA", "Argentina"),
                    ("BOLIVIA", "Bolivia"),
                    ("BRASIL", "Brasil"),
                    ("COLOMBIA", "Colombia"),
                    ("COSTA RICA", "Costa Rica"),
                    ("CUBA", "Cuba"),
                    ("CHILE", "Chile"),
                    ("ECUADOR", "Ecuador"),
                    ("EL SALVADOR", "El Salvador"),
                    ("GUATEMALA", "Guatemala"),
                    ("HONDURAS", "Honduras"),
                    ("MEXICO", "México"),
                    ("NICARAGUA", "Nicaragua"),
                    ("PANAMA", "Panamá"),
                    ("PARAGUAY", "Paraguay"),
                    ("PERU", "Perú"),
                    ("REPUBLICA DOMINICANA", "República Dominicana"),
                    ("URUGUAY", "Uruguay"),
                    ("VENEZUELA", "Venezuela"),
                ],
                default="Brasil",
                max_length=100,
            ),
        ),
    ]