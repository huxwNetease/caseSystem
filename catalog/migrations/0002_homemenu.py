# Generated by Django 2.0 on 2017-12-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuname', models.CharField(max_length=128, unique=True)),
                ('menulevel', models.IntegerField(default=0)),
                ('menuplevel', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '主页目录',
                'verbose_name_plural': '主页目录',
            },
        ),
    ]
