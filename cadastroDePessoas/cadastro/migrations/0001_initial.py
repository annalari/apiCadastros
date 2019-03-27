# Generated by Django 2.0.13 on 2019-03-27 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=45)),
                ('cep', models.BigIntegerField(max_length=8)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Bairro')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('cpf', models.IntegerField(max_length=11)),
                ('rg', models.IntegerField(max_length=20)),
                ('dataNascimento', models.DateField()),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Endereco')),
            ],
        ),
        migrations.AddField(
            model_name='endereco',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Pais'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Pais'),
        ),
        migrations.AddField(
            model_name='bairro',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Cidade'),
        ),
        migrations.AddField(
            model_name='bairro',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Pais'),
        ),
    ]