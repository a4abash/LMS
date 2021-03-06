# Generated by Django 2.2.4 on 2019-11-19 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('class_', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_suspended', models.BooleanField(default=False)),
                ('clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_.Class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
            options={
                'unique_together': {('clas', 'student')},
            },
        ),
    ]
