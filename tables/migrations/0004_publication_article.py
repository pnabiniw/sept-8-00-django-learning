# Generated by Django 4.2.5 on 2023-09-24 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_classroom_student_classroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=20)),
                ('publications', models.ManyToManyField(to='tables.publication')),
            ],
        ),
    ]
