# Generated by Django 5.1 on 2024-11-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_evolucion_date_register_alter_evolucion_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='evolucion',
            name='identification',
            field=models.CharField(default='default_value', max_length=20),
        ),
        migrations.AddField(
            model_name='evolucion',
            name='name',
            field=models.CharField(default='default_value', max_length=50),
            preserve_default=False,
        ),
    ]
