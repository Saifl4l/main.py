# Generated by Django 4.0.6 on 2022-07-27 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[('ASSETS', 'ASSETS'), ('LIABILTIES', 'LIABILTIES'), ('INCOME', 'INCOME'), ('EXPENSES', 'EXPENSES')], max_length=255)),
                ('code', models.CharField(max_length=25)),
                ('full_code', models.CharField(max_length=25)),
                ('extra', models.JSONField(blank=True, default=dict, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('invoice', 'invoice'), ('income', 'income'), ('expense', 'expense'), ('bill', 'bill')], max_length=25)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JoumiEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=25)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('IQD', 'IQD')], max_length=25)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joumi_entries', to='account.account')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.transaction')),
            ],
        ),
    ]