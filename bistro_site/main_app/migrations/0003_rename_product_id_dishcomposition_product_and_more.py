# Generated by Django 4.1.3 on 2023-01-13 09:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_dishcomposition_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dishcomposition',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='dishcomposition',
            name='dish_id',
        ),
        migrations.AddField(
            model_name='dishcomposition',
            name='dish',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.dish'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dishcomposition',
            name='record_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
