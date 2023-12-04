# Generated by Django 4.2.7 on 2023-11-27 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Barbearia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('sobre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Barbeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=90)),
                ('data_nasc', models.DateField()),
                ('descricao', models.TextField(blank=True, null=True)),
                ('barbearia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentoapp.barbearia')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('barbearia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentoapp.barbearia')),
            ],
        ),
        migrations.CreateModel(
            name='Imagem_cortes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='media/')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentoapp.servico')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
                ('ativo', models.BooleanField(default=True)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentoapp.agenda')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=90)),
                ('telefone', models.CharField(max_length=15)),
                ('data_nasc', models.DateField()),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Certificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=90)),
                ('arquivo', models.FileField(upload_to='arquivos')),
                ('barbeiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentoapp.barbeiro')),
            ],
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('F', 'Finalizado'), ('P', 'Pendente')], max_length=15)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentoapp.cliente')),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentoapp.horario')),
                ('servicos', models.ManyToManyField(to='agendamentoapp.servico')),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='barbeiro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentoapp.barbeiro'),
        ),
    ]
