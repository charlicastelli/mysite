# Generated by Django 4.1.7 on 2023-02-22 14:29

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
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(help_text='Nome da categoria', max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name_plural': 'Categorias',
                'db_table': 'tab_categoria',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoImovel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(help_text='Nome.', max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name_plural': 'Tipos de imóveis',
                'db_table': 'tab_tipoImovel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(help_text='Nome completo', max_length=200, verbose_name='Nome')),
                ('dataNascimento', models.DateField(help_text='dd/mm/aaaa', verbose_name='Data de nascimento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', help_text='Escolha o sexo', max_length=1, verbose_name='Sexo')),
                ('avatar', models.ImageField(blank=True, help_text='Escolha uma imagem', null=True, upload_to='media/avatar/%Y/%m/%d', verbose_name='Avatar')),
                ('status', models.BooleanField(default=True, verbose_name='Ativo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pessoas',
                'db_table': 'tab_pessoa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(help_text='Nome', max_length=50)),
                ('descricao', models.TextField(help_text='Descriçao do imóvel.')),
                ('status', models.BooleanField(default=True, verbose_name='Ativo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imobiliariaSA.categoria')),
                ('tipoImovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imobiliariaSA.tipoimovel')),
            ],
            options={
                'verbose_name_plural': 'Imóveis',
                'db_table': 'tab_imovel',
                'managed': True,
            },
        ),
    ]
