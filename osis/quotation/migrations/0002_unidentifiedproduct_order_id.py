# Generated by Django 4.2.5 on 2023-12-12 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidentifiedproduct',
            name='order_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quotation.order'),
            preserve_default=False,
        ),
    ]
