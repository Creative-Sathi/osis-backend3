# Generated by Django 4.2.5 on 2024-03-30 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellerdashboard', '0006_alter_productinfo_status_reviewproductinfo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='producttags',
            unique_together={('product', 'tagname')},
        ),
    ]
