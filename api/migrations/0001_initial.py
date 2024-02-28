# Generated by Django 4.2.7 on 2024-02-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=200)),
                ('salary', models.PositiveIntegerField()),
                ('age', models.PositiveIntegerField()),
                ('contact', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]