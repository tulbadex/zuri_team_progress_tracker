# Generated by Django 3.2.8 on 2021-11-01 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_stack_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='intern',
            options={'ordering': ('created_at',)},
        ),
    ]