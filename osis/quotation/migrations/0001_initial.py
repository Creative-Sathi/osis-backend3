# Generated by Django 4.2.5 on 2023-12-12 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sellerdashboard', '0002_productinfo_status'),
        ('profileseller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dateandtime', models.DateTimeField(auto_now_add=True)),
                ('requested_seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileseller.seller')),
            ],
        ),
        migrations.CreateModel(
            name='UnidentifiedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partNumber', models.CharField()),
                ('partName', models.CharField()),
                ('partCategories', models.CharField()),
                ('vehicleCompany', models.CharField()),
                ('brand', models.CharField()),
                ('model', models.CharField()),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SpecificSellerQuotation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField()),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('quoted_price', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotation.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellerdashboard.productinfo')),
                ('quoted_seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileseller.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotation.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellerdashboard.productinfo')),
                ('seller_quotation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quotation.specificsellerquotation')),
            ],
        ),
    ]
