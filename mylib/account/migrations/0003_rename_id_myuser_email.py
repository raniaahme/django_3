# Generated by Django 4.1.6 on 2023-02-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_id_myuser_idd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='IDDDD',
            new_name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
