# Generated by Django 5.2.1 on 2025-05-14 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ico_code', models.CharField(max_length=3, unique=True, verbose_name='ICO code')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='countries', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
    ]
