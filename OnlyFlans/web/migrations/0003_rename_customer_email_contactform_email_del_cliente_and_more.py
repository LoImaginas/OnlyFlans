# Generated by Django 5.0.4 on 2024-06-06 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contactform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='customer_email',
            new_name='email_del_cliente',
        ),
        migrations.RenameField(
            model_name='contactform',
            old_name='message',
            new_name='mensaje',
        ),
        migrations.RenameField(
            model_name='contactform',
            old_name='customer_name',
            new_name='nombre_del_cliente',
        ),
    ]