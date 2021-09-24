# Generated by Django 3.2.6 on 2021-09-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesandingredients', '0011_auto_20210908_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ing_amount', models.IntegerField()),
                ('ing_units', models.CharField(max_length=225)),
                ('ing_description', models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                'db_table': 'Ingredients_data',
            },
        ),
        migrations.CreateModel(
            name='RecipesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=225)),
                ('recipe_category', models.CharField(max_length=225)),
                ('recipe_yield_count', models.IntegerField()),
                ('yield_units', models.CharField(max_length=225)),
                ('other_ing_data', models.ManyToManyField(to='recipesandingredients.IngredientData')),
            ],
            options={
                'db_table': 'recipe_table',
            },
        ),
    ]