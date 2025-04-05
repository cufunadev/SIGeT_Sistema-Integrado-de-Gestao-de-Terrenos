# Generated by Django 5.2 on 2025-04-05 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terreno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=255)),
                ('metragem', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=15)),
                ('finalidade', models.CharField(choices=[('residencial', 'Residencial'), ('comercial', 'Comercial'), ('industrial', 'Industrial'), ('outro', 'Outro')], max_length=50)),
                ('status', models.CharField(default='disponível', max_length=50)),
            ],
        ),
    ]
