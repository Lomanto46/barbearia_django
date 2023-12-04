# Generated by Django 4.2.5 on 2023-12-02 18:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentoapp', '0005_horario_concluido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('conteudo', models.TextField(max_length=120)),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('barbeiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Feedback', to='agendamentoapp.barbeiro')),
            ],
        ),
    ]