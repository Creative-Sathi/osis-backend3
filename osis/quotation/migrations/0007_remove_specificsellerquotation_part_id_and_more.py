# Generated by Django 4.2.5 on 2023-12-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0006_quotation_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specificsellerquotation',
            name='part_id',
        ),
        migrations.RemoveField(
            model_name='specificsellerquotation',
            name='quantity',
        ),
        migrations.AddField(
            model_name='specificsellerquotation',
            name='remarks',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='specificsellerquotation',
            name='delivery_period',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='specificsellerquotation',
            name='quoted_per_per_unit_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='specificsellerquotation',
            name='quoted_price_per_unit',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
