# Generated by Django 3.0.8 on 2020-07-24 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200724_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.Product'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
