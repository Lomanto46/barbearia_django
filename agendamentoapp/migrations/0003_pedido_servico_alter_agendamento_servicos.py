# Generated by Django 4.2.7 on 2023-12-01 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentoapp', '0002_remove_barbeiro_barbearia_remove_barbeiro_descricao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido_servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentoapp.servico')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentoapp.cliente')),
            ],
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='servicos',
            field=models.ManyToManyField(to='agendamentoapp.pedido_servico'),
        ),
    ]