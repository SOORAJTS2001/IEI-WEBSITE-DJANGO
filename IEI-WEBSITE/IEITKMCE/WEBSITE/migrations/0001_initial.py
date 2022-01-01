# Generated by Django 4.0 on 2021-12-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Exam1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam', models.CharField(max_length=2500)),
                ('Authority', models.CharField(max_length=2500)),
                ('Regno', models.CharField(max_length=2500)),
                ('YearofPassing', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Exam2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam', models.CharField(max_length=2500)),
                ('Authority', models.CharField(max_length=2500)),
                ('Regno', models.CharField(max_length=2500)),
                ('YearofPassing', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Exam3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam', models.CharField(max_length=2500)),
                ('Authority', models.CharField(max_length=2500)),
                ('Regno', models.CharField(max_length=2500)),
                ('YearofPassing', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=2500)),
                ('Branch', models.CharField(choices=[('EEE', 'EEE'), ('EC', 'EC'), ('MEC', 'MEC'), ('CHEM', 'CHEM'), ('CS', 'CS'), ('MECHPRO', 'MECHPRO'), ('CIVIL', 'CIVIL')], default='EEE', max_length=2500)),
                ('Father', models.CharField(max_length=2500)),
                ('Address', models.TextField(max_length=2500)),
                ('Email', models.CharField(max_length=2500)),
                ('Number', models.CharField(max_length=2500)),
                ('Nationality', models.CharField(max_length=2500)),
                ('College', models.CharField(max_length=2500)),
                ('Year', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=2500)),
            ],
        ),
    ]
