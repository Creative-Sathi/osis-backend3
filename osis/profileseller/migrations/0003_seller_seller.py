# Generated by Django 4.2.5 on 2024-02-15 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profileseller', '0002_seller_remarks_seller_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]