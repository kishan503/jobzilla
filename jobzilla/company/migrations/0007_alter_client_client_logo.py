# Generated by Django 3.2.9 on 2021-12-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_client_client_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_logo',
            field=models.FileField(default='media/userdefault.png', upload_to='media/images/'),
        ),
    ]
