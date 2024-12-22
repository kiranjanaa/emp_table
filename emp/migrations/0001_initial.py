# Generated by Django 5.1.3 on 2024-12-22 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptid', models.IntegerField(primary_key=100, serialize=False)),
                ('deptname', models.CharField(max_length=100)),
                ('deptloc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('sal', models.DecimalField(decimal_places=3, max_digits=10)),
                ('comm', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('hiredate', models.DateField()),
                ('deptid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.dept')),
                ('mgr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='emp.emp')),
            ],
        ),
    ]