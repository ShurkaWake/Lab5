# Generated by Django 4.2.1 on 2023-05-11 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_order_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_item',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.order'),
        ),
    ]
