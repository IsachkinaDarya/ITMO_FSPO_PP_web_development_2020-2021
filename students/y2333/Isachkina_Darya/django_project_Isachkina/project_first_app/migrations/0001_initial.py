# Generated by Django 3.1.6 on 2021-02-21 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gos_number', models.CharField(max_length=15)),
                ('mark', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_day', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Own',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField(blank=True)),
                ('id_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car')),
                ('id_CarOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowner')),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_num', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('date_issue', models.DateTimeField()),
                ('id_CarOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowner')),
            ],
        ),
    ]
