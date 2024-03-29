# Generated by Django 4.0.4 on 2022-05-12 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('issuesApp', '0004_alter_issues_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='priority_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.priority'),
        ),
        migrations.AlterField(
            model_name='issues',
            name='serverity_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.serverity'),
        ),
        migrations.AlterField(
            model_name='issues',
            name='status_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.status'),
        ),
    ]
