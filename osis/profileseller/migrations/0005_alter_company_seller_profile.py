# Generated by Django 4.2.5 on 2024-02-27 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileseller', '0004_remove_documents_businessdocument_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='seller_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileseller.sellerprofile'),
        ),
    ]