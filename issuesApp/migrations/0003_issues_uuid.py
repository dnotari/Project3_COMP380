# Generated by Django 4.0.4 on 2022-05-12 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuesApp', '0002_rename_priority_issues_priority_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='issues',
            name='uuid',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
