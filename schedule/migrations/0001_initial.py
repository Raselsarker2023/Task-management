# Generated by Django 5.0 on 2024-03-17 15:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('reminder_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Draft', 'Draft'), ('Ongoing', 'Ongoing'), ('Abandon', 'Abandon'), ('Completed', 'Completed')], max_length=20, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('cancel_reason', models.CharField(blank=True, max_length=150, null=True)),
                ('admin_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
