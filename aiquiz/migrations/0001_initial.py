# Generated by Django 5.1.6 on 2025-02-13 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('creater', models.CharField(blank=True, max_length=50, null=True)),
                ('question_file', models.FileField(upload_to='Store')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField(blank=True, null=True)),
                ('total_marks', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
