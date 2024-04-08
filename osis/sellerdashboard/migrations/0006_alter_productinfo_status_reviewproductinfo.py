# Generated by Django 4.2.5 on 2024-03-30 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileseller', '0007_alter_sellerprofile_storelogo_and_more'),
        ('sellerdashboard', '0005_alter_productinfo_part_id_alter_productinfo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='status',
            field=models.CharField(),
        ),
        migrations.CreateModel(
            name='reviewproductinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_id', models.CharField()),
                ('normalRate', models.CharField()),
                ('bulkRate', models.CharField(blank=True, null=True)),
                ('stockQuantity', models.CharField()),
                ('units', models.CharField()),
                ('status', models.CharField(default='Reviewed')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewproducts', to='profileseller.seller')),
            ],
        ),
    ]
