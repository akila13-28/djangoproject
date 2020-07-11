# Generated by Django 3.0.8 on 2020-07-11 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField(null=True)),
                ('heading', models.CharField(max_length=100)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('ques', models.TextField(null=True)),
                ('desc', models.TextField(null=True)),
            ],
        ),
    ]
