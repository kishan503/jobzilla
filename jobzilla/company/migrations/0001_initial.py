# Generated by Django 3.2.9 on 2021-11-15 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
                ('otp', models.IntegerField(default=459)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verfied', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('company_address', models.CharField(max_length=100)),
                ('company_contact', models.CharField(max_length=20)),
                ('company_city', models.CharField(max_length=30)),
                ('company_type', models.CharField(max_length=30)),
                ('company_logo', models.FileField(default='default.jpg', upload_to='media/images/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.user')),
            ],
        ),
    ]
