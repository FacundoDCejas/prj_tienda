# Generated by Django 3.2.6 on 2021-09-10 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_articulo_cargo_cliente_empleado_item_movimiento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='Legajo',
            new_name='legajo',
        ),
    ]
