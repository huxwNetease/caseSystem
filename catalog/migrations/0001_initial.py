# Generated by Django 2.0 on 2017-12-19 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuname', models.CharField(max_length=128, unique=True)),
                ('menulevel', models.IntegerField(default=0)),
                ('menuplevel', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '目录',
                'verbose_name_plural': '目录',
            },
        ),
    ]