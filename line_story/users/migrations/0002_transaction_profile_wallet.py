# Generated by Django 4.0.4 on 2022-05-31 23:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='amount')),
                ('descriptions', models.CharField(max_length=255, verbose_name='transaction description')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balance_changes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='phone number must not consist of space and requires country code. eg : +79546748973', regex='^\\+?1?\\d{9,15}$')], verbose_name='phone')),
                ('region', models.CharField(max_length=255, verbose_name='region of residence')),
                ('image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.file', verbose_name='profile photo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ballance', models.PositiveIntegerField(default=0, verbose_name='user balance')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL, verbose_name='user`s wallet')),
            ],
            options={
                'permissions': (('can_add_money', 'top up balance'),),
                'unique_together': {('user', 'id')},
            },
        ),
    ]