# Generated by Django 4.0.3 on 2022-03-25 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_products_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the product type.', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='product_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='main.producttypes'),
            preserve_default=False,
        ),
    ]