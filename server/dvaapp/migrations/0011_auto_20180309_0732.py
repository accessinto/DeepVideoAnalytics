# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-09 07:32
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0010_remove_video_youtube_video'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='indexentries',
            unique_together=set([('video', 'features_file_name')]),
        ),
        migrations.AddField(
            model_name='indexentries',
            name='entries',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='indexentries',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='framelist',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='retriever',
            name='algorithm',
            field=models.CharField(choices=[('L', 'LOPQ'), ('E', 'Exact'), ('F', 'FAISS')], db_index=True, default='E', max_length=1),
        ),
        migrations.RemoveField(
            model_name='indexentries',
            name='entries_file_name',
        ),
    ]
