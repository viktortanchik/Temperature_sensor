# Generated by Django 3.2.5 on 2021-07-03 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scripts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='vin')),
                ('weatherstation', models.CharField(max_length=64, verbose_name='weatherstation')),
            ],
        ),
        migrations.CreateModel(
            name='Temp3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperature', models.CharField(default='100', max_length=64, verbose_name='Temperature')),
                ('Humidity', models.CharField(default='100', max_length=64, verbose_name='Humidity')),
                ('Temp3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Temp3', to='temp.scripts')),
            ],
        ),
        migrations.CreateModel(
            name='Temp2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperature', models.CharField(default='100', max_length=64, verbose_name='Temperature')),
                ('Humidity', models.CharField(default='100', max_length=64, verbose_name='Humidity')),
                ('Temp2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Temp2', to='temp.scripts')),
            ],
        ),
        migrations.CreateModel(
            name='Temp1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperature', models.CharField(default='100', max_length=64, verbose_name='Temperature')),
                ('Humidity', models.CharField(default='100', max_length=64, verbose_name='Humidity')),
                ('Temp1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Temp1', to='temp.scripts')),
            ],
        ),
    ]