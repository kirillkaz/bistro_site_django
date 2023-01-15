# Generated by Django 4.1.3 on 2023-01-14 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_product_id_dishcomposition_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='main_app.recipe'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='img',
            field=models.ImageField(upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]
