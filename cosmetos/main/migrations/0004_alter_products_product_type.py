# Generated by Django 4.0.3 on 2022-03-25 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_producttypes_products_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='main.producttypes'),
        ),
    ]
