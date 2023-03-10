# Generated by Django 4.1.3 on 2022-11-29 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_ingredient_unit_recipeingredientunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredientunit',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients_units', to='recipes.recipe'),
        ),
    ]
