# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 15:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=127, unique=True, validators=[django.core.validators.RegexValidator(message='Only lower case letters, numbers, slashes (/) and dashes (-) allowed.', regex='[a-z0-9-]+')])),
                ('name', models.CharField(max_length=63)),
                ('type', models.CharField(default='aws', max_length=12)),
                ('email', models.EmailField(help_text='E-mail address of the Root Account Credentials', max_length=254, verbose_name='E-mail address')),
                ('managed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='cmdb.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='node',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='cmdb.Account'),
        ),
    ]
