# Generated by Django 4.0.4 on 2022-05-12 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
        ('issuesApp', '0005_alter_issues_priority_id_alter_issues_serverity_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actionitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=40, null=True)),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('date_assigned', models.DateField(blank=True, null=True)),
                ('expected_completion_date', models.DateField(blank=True, null=True)),
                ('actual_completion_date', models.DateField(blank=True, null=True)),
                ('status_description', models.TextField(blank=True, null=True)),
                ('update_date', models.DateField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('issue_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='issuesApp.issues')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.status')),
            ],
            options={
                'db_table': 'ACTIONITEMS',
            },
        ),
    ]
