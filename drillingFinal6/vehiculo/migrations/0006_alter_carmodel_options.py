# Generated by Django 4.2.17 on 2024-12-15 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0005_alter_carmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'permissions': (('es_miembro_1', 'Es miembro con prioridad 1'), ('development', 'Puede desarrollar'), ('scrum_master', 'Es Scrum Master'), ('product_owner', 'Es Product Owner'), ('visualizar_catalogo', 'Puede visualizar Catálogo de Vehículos'))},
        ),
    ]
