# Generated by Django 4.0.4 on 2022-05-31 23:48

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='quantity of goods reserved')),
                ('is_reserved', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='number of products in the order')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='total order price')),
                ('product_list', models.JSONField()),
                ('address', models.CharField(blank=True, max_length=1800, null=True, verbose_name='address')),
                ('is_active', models.BooleanField(default=True, verbose_name='active order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantity of product in the cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'cart item',
                'verbose_name_plural': 'carts items',
            },
        ),
    ]
