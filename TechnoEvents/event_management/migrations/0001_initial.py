# Generated by Django 3.1.3 on 2020-11-12 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('description', models.TextField(max_length=500)),
                ('organiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.user')),
            ],
        ),
    ]
