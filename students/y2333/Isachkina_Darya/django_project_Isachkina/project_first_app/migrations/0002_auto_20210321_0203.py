# Generated by Django 3.1.7 on 2021-03-20 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='ownership',
            field=models.ManyToManyField(through='project_first_app.Own', to='project_first_app.CarOwner'),
        ),
    ]
