# Generated by Django 4.0.6 on 2022-07-27 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_joumientry_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JoumiEntry',
            new_name='JournalEntry',
        ),
    ]
