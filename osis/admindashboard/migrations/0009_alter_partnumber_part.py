# Generated by Django 4.2.5 on 2024-03-13 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0008_remove_partinfo_partnumber_partnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnumber',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partnumbers', to='admindashboard.partinfo'),
        ),
    ]