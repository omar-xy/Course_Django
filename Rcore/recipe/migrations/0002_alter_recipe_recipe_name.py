# Generated by Django 4.2.15 on 2024-10-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_name',
            field=models.CharField(default='Unnamed Recipe', max_length=255),
        ),
    ]