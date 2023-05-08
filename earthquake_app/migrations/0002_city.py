# Generated by Django 3.2.10 on 2023-05-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthquake_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('population', models.IntegerField()),
            ],
            options={
                'db_table': 'city',
                'abstract': False,
            },
        ),
    ]
