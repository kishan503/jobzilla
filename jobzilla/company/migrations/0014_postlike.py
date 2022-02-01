# Generated by Django 3.2.9 on 2021-12-13 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_auto_20211213_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.client')),
                ('jobPost_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.jobpost')),
            ],
        ),
    ]