# Generated by Django 2.2.13 on 2020-06-12 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_recipe_contained_allergen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='contained_allergen',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
