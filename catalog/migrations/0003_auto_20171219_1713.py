# Generated by Django 2.0 on 2017-12-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_homemenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoiceMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuname', models.CharField(max_length=128, unique=True)),
                ('menulevel', models.IntegerField(default=0)),
                ('menuplevel', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '音源目录',
                'verbose_name_plural': '音源目录',
            },
        ),
        migrations.CreateModel(
            name='WordMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuname', models.CharField(max_length=128, unique=True)),
                ('menulevel', models.IntegerField(default=0)),
                ('menuplevel', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '词条目录',
                'verbose_name_plural': '词条目录',
            },
        ),
        migrations.RenameModel(
            old_name='Menu',
            new_name='PictureMenu',
        ),
        migrations.AlterModelOptions(
            name='picturemenu',
            options={'verbose_name': '图片目录', 'verbose_name_plural': '图片目录'},
        ),
    ]
