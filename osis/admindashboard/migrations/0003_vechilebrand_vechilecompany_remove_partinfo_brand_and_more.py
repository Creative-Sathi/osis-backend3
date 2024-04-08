# Generated by Django 4.2.5 on 2023-12-27 11:32

import admindashboard.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0002_remove_partinfo_sellingprice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='vechileBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('image', models.ImageField(blank=True, upload_to=admindashboard.models.unique_filename)),
            ],
        ),
        migrations.CreateModel(
            name='vechileCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('image', models.ImageField(blank=True, upload_to=admindashboard.models.unique_filename)),
            ],
        ),
        migrations.RemoveField(
            model_name='partinfo',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='partinfo',
            name='manufactureYear',
        ),
        migrations.RemoveField(
            model_name='partinfo',
            name='model',
        ),
        migrations.RemoveField(
            model_name='partinfo',
            name='partCategories',
        ),
        migrations.RemoveField(
            model_name='partinfo',
            name='subCategory',
        ),
        migrations.RemoveField(
            model_name='partinfo',
            name='vehicleCompany',
        ),
        migrations.CreateModel(
            name='vechileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('image', models.ImageField(blank=True, upload_to=admindashboard.models.unique_filename)),
                ('vechileBrand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='admindashboard.vechilebrand')),
            ],
        ),
        migrations.AddField(
            model_name='vechilebrand',
            name='vechileCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='admindashboard.vechilecompany'),
        ),
        migrations.CreateModel(
            name='partCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('image', models.ImageField(blank=True, upload_to=admindashboard.models.unique_filename)),
                ('vechileModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='admindashboard.vechilemodel')),
            ],
        ),
        migrations.AddField(
            model_name='partinfo',
            name='partCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='admindashboard.partcategory'),
            preserve_default=False,
        ),
    ]