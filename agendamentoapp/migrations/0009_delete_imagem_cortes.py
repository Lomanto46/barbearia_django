# Generated by Django 4.2.5 on 2023-12-03 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentoapp', '0008_remove_agendamento_status_agendamento_finalizado'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Imagem_cortes',
        ),
    ]
