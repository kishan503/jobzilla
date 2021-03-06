# Generated by Django 3.2.9 on 2021-12-08 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20211203_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, null=True, upload_to='media/images/')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
