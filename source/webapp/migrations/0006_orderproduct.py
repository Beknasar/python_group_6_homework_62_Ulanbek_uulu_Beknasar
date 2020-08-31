# Generated by Django 2.2 on 2020-08-31 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20200830_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Количество заказанных продуктов')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='webapp.Order', verbose_name='Заказы продуктов')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordering_product', to='webapp.Product', verbose_name='Продукты в заказах')),
            ],
        ),
    ]
