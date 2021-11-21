# Generated by Django 3.2.9 on 2021-11-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('isbn', models.TextField()),
                ('number_of_pages', models.IntegerField()),
                ('publisher', models.TextField()),
                ('country', models.TextField()),
                ('release_date', models.DateField()),
                ('authors', models.ManyToManyField(to='managebook.Author')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]