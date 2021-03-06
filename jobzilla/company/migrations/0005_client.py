# Generated by Django 3.2.9 on 2021-11-30 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_company_company_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30)),
                ('client_address', models.CharField(max_length=100)),
                ('client_contact', models.CharField(max_length=20)),
                ('client_qualification', models.CharField(max_length=30)),
                ('client_gender', models.CharField(max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.user')),
            ],
        ),
    ]
