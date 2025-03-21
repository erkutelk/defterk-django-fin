# Generated by Django 5.1.6 on 2025-03-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Muhasebe', '0004_alter_fatura_bilgileri_kategori'),
    ]

    operations = [
        migrations.CreateModel(
            name='musteriler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('surname', models.CharField(max_length=10)),
                ('telefon', models.CharField(max_length=11)),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('durum', models.BooleanField(default=True)),
            ],
        ),
    ]
