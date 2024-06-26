# Generated by Django 4.2.5 on 2024-03-17 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0009_alter_partnumber_part'),
        ('sellerdashboard', '0004_rename_sellingprice_productinfo_normalrate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='part_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Part', to='admindashboard.partinfo'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='status',
            field=models.CharField(default='Reviewed'),
        ),
    ]
