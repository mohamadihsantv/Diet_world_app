# Generated by Django 5.1.6 on 2025-03-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_species_fooditem_category_fooditem_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='species',
        ),
        migrations.AlterField(
            model_name='species',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='species',
            field=models.ManyToManyField(blank=True, to='product.species'),
        ),
    ]
